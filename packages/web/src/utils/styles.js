export const mergeStyles = (localClasses, classes) => {
  const lc = localClasses || {};
  const c = classes || {};
  const keys = [...new Set([...Object.keys(lc), ...Object.keys(c)])];
  return keys.reduce((acc, key) => {
    acc[key] = [lc[key], c[key]].filter((value) => value).join(" ");
    return acc;
  }, {});
};
