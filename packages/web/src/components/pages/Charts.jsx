import { makeStyles, Paper } from '@material-ui/core';
import React, {useState} from 'react';
import { fetchDevices } from '../../utils/fetch';
import PageLoader from '../../views/PageLoader';

export default function Charts({classes = {}}) {
    const localClasses = useStyles();
    const allClasses = {
        root: [localClasses.root, classes.root].filter(c => c).join(' ')
    }

    const [devices, setDevices] = useState([]);

    if (devices.length === 0) {
        fetchDevices().then(setDevices)
    }
    

    return <Paper className={allClasses.root} elevation={0}>
        {devices.length === 0 && <PageLoader /> }
        {devices.length > 0 && <div>
            TODO: https://material-ui.com/components/grid-list/
            </div>}
    </Paper>

}


const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex'
    },
    progress: {

    }
}))