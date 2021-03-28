import logo from './logo.svg';
import "@fontsource/roboto";
import './App.css';

import {AppBar, Toolbar, Typography, Button, IconButton} from '@material-ui/core'
import {MenuIcon} from '@material-ui/icons/MenuIcon'
import {makeStyles} from '@material-ui/icons'

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

function App() {
  const classes = useStyles();
  return (
    <div className="App">
      <AppBar position="static">
  <Toolbar>
    <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
      <MenuIcon />
    </IconButton>
    <Typography variant="h6" className={classes.title}>
      News
    </Typography>
    <Button color="inherit">Login</Button>
  </Toolbar>
</AppBar>
    </div>
  );
}

export default App;
