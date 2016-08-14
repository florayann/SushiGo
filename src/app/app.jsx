import React from 'react';
import ReactDOM from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import injectTapEventPlugin from 'react-tap-event-plugin';
import AppBar from 'material-ui/AppBar';

injectTapEventPlugin();

const SushiGoAppBar = () => (
    <AppBar
	title="Sushi Go"
    />
);


const App = () => (
    <MuiThemeProvider>
	<SushiGoAppBar/>
    </MuiThemeProvider>
);

ReactDOM.render(
    <App />,
    document.getElementById('app')
);
