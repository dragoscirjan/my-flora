import { CircularProgress, makeStyles, Paper } from '@material-ui/core';
import React from 'react';

export default function Charts({classes = {}}) {
    const localClasses = useStyles();
    const allClasses = {
        root: [localClasses.root, classes.root].filter(c => c).join(' ')
    }

    return <Paper className={allClasses.root} elevation={0}>
        <CircularProgress />
    </Paper>

}


const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex'
    },
    progress: {

    }
}))