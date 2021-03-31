import { CircularProgress, makeStyles } from '@material-ui/core';



export default function PageLoader({classes = {}}) {
    const localClasses = useStyles();
    const allClasses = {
        root: [localClasses.root, classes.root].filter(c => c).join(' ')
    }


    return <div className={allClasses.root}>
        <CircularProgress />
    </div>
}


const useStyles = makeStyles((theme) => ({
    root: {
        alignItems: 'center',
        display: 'flex',
        // this is not the proper way to do it
        height: 'calc(100vh - 64px)',
        justifyContent: 'center',
        width: '100%',
    }
}))