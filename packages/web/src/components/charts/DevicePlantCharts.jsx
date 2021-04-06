import AreaClosed from "../chart/AreaClosed";
import { makeStyles } from "@material-ui/core";
import { mergeStyles } from "../../utils/styles";
import React, { createRef, useState } from "react";

export default function DevicePlantCharts({ classes, device }) {
  const localClasses = mergeStyles(useStyles(), classes);

  const ref = createRef();

  const [width, setWitdh] = useState(160);
  const [height, setHeight] = useState(100);
  const [haveWidth, setHaveWidth] = useState(false);

  if (width <= 160) {
    setTimeout(() => {
      if (ref.current?.offsetWidth) {
        const w = ref.current?.offsetWidth;
        setWitdh(w - 24);
        setHeight(Math.ceil((w * 10) / 16 / 1.5));
        setHaveWidth(true);
      }
    }, 200);
  }

  return (
    <div ref={ref} className={localClasses.root}>
      <h2>{device.address}</h2>
      {haveWidth && <AreaClosed width={width} height={height} />}
    </div>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
}));
