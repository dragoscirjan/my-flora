import json5 from "json5";
import config from "../config";

export const fetchDevices = () =>
  fetch(`${config.endpoint}${config.paths.devices}`)
    .then((response) => response.text())
    .then(json5);
