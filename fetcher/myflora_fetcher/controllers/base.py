from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
from ..pollers import PollerFactory, MiPoller, PollerAdapters, BluetoothAdapters
from miflora.miflora_poller import MiFloraPoller
from btlewrap.bluepy import BluepyBackend
from btlewrap.pygatt import PygattBackend

VERSION_BANNER = """
Query Xiaomi Flora devices & store data to designated services %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Query Xiaomi Flora devices & store data to designated services'

        # text displayed at the bottom of --help output
        epilog = 'Usage: myflora_fetcher command1 --foo bar'

        # controller level arguments. ex: 'myflora_fetcher --version'
        arguments = [
            ### add a version banner
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='fetch --mac <mac:address>',

        # sub-command level arguments. ex: 'myflora_fetcher command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-m', '--mac'],
             {'help': 'mac address of the bluetooth device',
              'action': 'store',
              'dest': 'mac'}),
            (['-t', '--type'],
             {'help': 'bluetooth device type: {}'.format(PollerAdapters.mi),
              'action': 'store',
              'dest': 'type'}),
            (['-bt', '--btlib'],
             {'help': 'bluetooth library: {},{}'.format(BluetoothAdapters.bluepy, BluetoothAdapters.pygatt),
              'action': 'store',
              'dest': 'backend'}),
            (['-c', '--clear'],
             {'help': 'clear data on device',
              'action': 'store_true',
              'default': False,
              'dest': 'clear'}),
        ],
    )
    def fetch(self):
        """Example sub-command."""

        data = {
            'mac': '',
            'type': PollerAdapters.mi,
            'backend': BluetoothAdapters.bluepy,
            'clear': False
        }

        args = self.app.pargs.__dict__
        for key in data.keys():
            if args[key] is not None:
                data[key] = args[key]

        self.app.log.info(data)

        backend = BluepyBackend if data['backend'] == BluetoothAdapters.bluepy else PygattBackend
        poller = PollerFactory.get_instance(MiPoller,
                                            mac=data['mac'],
                                            poller=MiFloraPoller(mac=data['mac'], backend=backend))

        self.app.log.info(poller)

        history_items = poller.get_history_items()

        for item in history_items:
            self.app.log.info(item)

        # self.app.render(data, 'command1.jinja2')
