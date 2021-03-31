import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";

import "./App.css";
import '@fontsource/roboto';

import Logo from "./views/Logo";
import Charts from "./components/pages/Charts";

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexDirection: 'column',
    height: '100vh'
  },
}));

function App() {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Logo />
          <Typography variant="h6" className={classes.title}>
            My Flora
          </Typography>
        </Toolbar>
      </AppBar>
      <Charts />
    </div>
  );
}

export default App;
