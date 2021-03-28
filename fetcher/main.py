"""CLI main runner"""
from flora.di import container
import cherrypy
import json


def jsonify_error(status, message, traceback, version): # pylint: disable=unused-argument
  """JSONify all CherryPy error responses (created by raising the
  cherrypy.HTTPError exception)
  """

  cherrypy.response.headers['Content-Type'] = 'application/json'
  response_body = json.dumps({
    'error': {
      'http_status': status,
      'message': message,
    }
  })

  cherrypy.response.status = status

  return response_body


def main():
  """main runner"""
  cp_config = {
      '/': {
          'request.dispatch': container.route_dispatcher().build(),
          # 'error_page.default': jsonify_error,
          'cors.expose.on': True,
          # 'tools.auth_basic.on': True,
          # 'tools.auth_basic.realm': 'localhost',
          # 'tools.auth_basic.checkpassword': validate_password,
      },
  }

  cherrypy.tree.mount(root=None, config=cp_config)

  cherrypy.config.update({
      # 'server.socket_host': '0.0.0.0',
      # 'server.socket_port': 8080,
  })

  cherrypy.engine.start()
  cherrypy.engine.block()


if __name__ == '__main__':
  main()
