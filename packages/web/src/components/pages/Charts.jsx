import { makeStyles, Grid, Paper } from "@material-ui/core";
import React, { useState } from "react";
import { fetchDevices } from "../../utils/fetch";
import { mergeStyles } from "../../utils/styles";
import PageLoader from "../../views/PageLoader";
import DevicePlantCharts from "../charts/DevicePlantCharts";

export default function Charts({ classes = {} }) {
  const localClasses = mergeStyles(useStyles(), classes);

  const [devices, setDevices] = useState([]);

  if (devices.length === 0) {
    fetchDevices()
      .then((result) => result.devices)
      .then(setDevices);
  }

  return (
    <Paper className={localClasses.root} elevation={0}>
      {devices.length === 0 && <PageLoader />}
      {devices && devices.length > 0 && (
        <div className={localClasses.grid}>
          <Grid container spacing={3}>
            {devices.map((device) => (
              <Grid item xs={12} sm={6} xl={4} key={device.address}>
                <Paper>
                  <DevicePlantCharts device={device} />
                </Paper>
              </Grid>
            ))}
          </Grid>
        </div>
      )}
    </Paper>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
  },
  progress: {},
  grid: {
    display: "flex",
    padding: "12px",
    width: "calc(100% - 24px)",
  },
}));
