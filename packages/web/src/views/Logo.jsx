import { createSvgIcon, SvgIcon } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import * as React from "react";

const useStyles = makeStyles((theme) => ({
  root: {
    display: "block",
    marginRight: "20px",
    "& g": {
      fill: "#FFFFFF",
    },
  },
}));

export default function Logo({ classes = {}, title = "My Flora" }) {
  const localClasses = useStyles();
  const allClasses = {
    root: [localClasses.root, classes.root].filter((c) => c).join(" "),
  };
  return (
    <i className={allClasses.root}>
      <MyFloraLogo />
    </i>
  );
}

const MyFloraLogo = ({ displayName = "MyFloraLogo", ref, ...props }) => (
  <SvgIcon
    data-testid={`${displayName}Icon`}
    ref={ref}
    width="864px"
    height="864px"
    viewBox="0 0 864 864"
    {...props}
  >
    <g>
      <path
        d="M405.5536,166.0404c-19.8176-35.1744-49.6074-64.3553-85.2893-83.5433h-0.0002
		c-39.0002-16.9652-83.1909-23.5583-126.9673-18.5776c-32.7285,60.7706-38.0532,133.2928-15.3423,195.6351
		c17.0049,39.0775,45.218,72.9002,80.7073,96.7523c35.51,23.8176,77.6169,37.2066,120.4482,38.3017l-0.0056-0.001
		c-42.7168-5.5211-82.1104-23.2585-112.9675-49.3052c-30.8464-26.0645-52.8196-60.1805-63.6497-96.2746
		c-16.9668-55.0235-9.6619-112.6673,13.5503-151.2026c2.1025,0.2033,4.1892,0.4568,6.2588,0.7603
		c24.4424-1.7136,52.946,3.3225,80.6689,15.7086c31.5051,12.1721,60.6038,34.1252,81.8179,63.2881
		c20.0667,27.5833,33.04,61.54,36.1086,97.5931c3.052,36.0536-3.8083,73.8317-20.8074,108.2364
		c20.3604-32.3128,31.7263-69.8297,32.7017-107.9402C433.7289,237.3589,424.2634,199.3231,405.5536,166.0404z"
      />
      <path
        d="M606.9438,180.9526c-50.9956,14.8234-97.2634,44.2089-132.2175,83.9683c-34.9204,39.7831-57.9663,89.3062-65.8557,141.5143
		c12.2939-51.5492,39.3477-97.8628,75.9231-132.7833c36.5867-34.9078,82.3862-58.103,129.6406-67.2054
		c72.1736-14.3479,145.905,2.5452,194.6458,38.8652c-0.4976,2.7168-1.0576,5.4112-1.6782,8.0811
		c-2.1396,33.2204-13.9177,69.3919-34.926,102.4943c-21.6492,37.4005-55.0564,69.601-95.7605,90.5563
		c-38.5005,19.8215-83.4287,29.5541-128.8713,26.7969c-45.4426-2.773-91.0046-17.9945-130.3762-44.7363
		c36.8706,29.7972,81.6172,49.4304,128.6167,56.4281c47.0049,6.9657,95.5762,1.1943,139.6021-16.5882
		c46.5388-18.8412,87.2463-50.8287,116.4194-91.4879c27.3611-44.2079,42.7065-96.4177,43.6382-149.8028
		C775.9694,178.613,687.1274,161.84,606.9438,180.9526z"
      />
      <polygon points="408.8698,406.44 408.8705,406.4352 408.8698,406.4383 	" />
      <path
        d="M19.5431,630.6216c64.4473,34.0452,141.2656,39.402,207.2163,15.4767c41.3301-17.8917,77.0645-47.4861,102.2205-84.6614
		c25.1035-37.1748,39.158-81.2047,40.2092-125.9617c-5.7341,44.6439-24.3965,85.8525-51.873,118.1693
		c-27.5125,32.3276-63.5791,55.3986-101.7705,66.826c-58.2219,17.8982-119.2822,10.4282-160.1567-13.7308
		c0.2092-2.1984,0.4719-4.3809,0.7869-6.5455c-1.885-25.5466,3.3662-55.3666,16.4026-84.3882
		c12.7979-32.9679,35.9641-63.4586,66.7849-85.7234c29.1497-21.0589,65.0718-34.7206,103.2417-38.0329
		c38.1704-3.2943,78.1943,3.7684,114.6768,21.4424c-34.2739-21.194-74.0386-32.97-114.3992-33.8797
		c-40.3638-0.8772-80.6135,9.1293-115.8049,28.7873c-37.1963,20.8226-68.0112,52.0523-88.2278,89.4152l0,0
		C20.996,538.6472,14.1418,584.8652,19.5431,630.6216L19.5431,630.6216z"
      />
      <path
        d="M369.1918,435.3921c-0.0005,0.0276-0.002,0.0553-0.0027,0.0832c0.0037-0.0289,0.0083-0.0575,0.012-0.0861
		L369.1918,435.3921z"
      />
      <path
        d="M532.4409,504.7565c-33.0217-27.1229-73.626-44.5008-116.1489-49.7121l0.0056,0.0015
		c41.9778,9.6056,79.4575,31.0502,107.6306,59.9442c28.1611,28.9101,46.7061,64.9804,53.9673,101.9468
		c11.5244,56.3976-1.3643,113.0676-28.2231,149.1879c-2.073-0.4046-4.1252-0.8578-6.1553-1.3587
		c-24.4946-0.6465-52.3735-8.4019-78.7588-23.3977c-30.1707-15.1465-56.9932-39.7965-75.2651-70.8639
		c-17.2837-29.3846-26.8867-64.4302-26.427-100.6087c0.4763-36.1778,10.9863-73.1185,31.2588-105.7256
		c-23.4141,30.2016-38.3833,66.4488-43.0684,104.2861c-4.6531,37.8427,1.061,76.6103,16.439,111.537
		c16.2961,36.916,43.1018,68.8267,76.7458,91.3581l0,0c37.1636,20.6382,80.5039,31.4529,124.5601,30.7081
		c38.4978-57.3354,50.8657-129.0048,34.3376-193.2391C590.2226,568.2903,565.4387,531.9114,532.4409,504.7565z"
      />
      <path
        d="M139.1235,551.8256c28.4002,17.5334,62.9766,11.4949,89.4002,1.1382c26.4167-10.3734,58.5212-28.3203,72.8333-64.0901
		s32.3091-43.5811,45.252-58.3019c-17.7705,5.9604-67.0852,33.9576-93.6265,77.0235
		C230.3334,544.3456,167.6208,554.5843,139.1235,551.8256z"
      />
      <path
        d="M290.2946,239.3326c4.9714,27.7886,16.2798,62.6236,48.7085,83.6813s36.5496,40.1373,48.491,55.6713
		c-2.3406-18.4909-20.1348-72.0848-57.3242-106.5034c-31.7361-29.371-29.3486-92.4761-20.9541-119.6764
		C286.2692,176.6697,285.341,211.5406,290.2946,239.3326z"
      />
      <path
        d="M654.1752,340.8556c-23.688-23.4467-58.7441-25.3132-86.8379-21.146c-28.0908,4.1854-63.4419,14.4743-85.5049,46.1145
		c-22.0632,31.6404-41.3696,35.2169-57.3206,46.6571c18.6655-1.824,73.0647-18.0467,108.698-54.0542
		C563.6179,327.7,627.0385,331.7811,654.1752,340.8556z"
      />
      <path
        d="M406.6083,563.7626c6.5615,27.4609,19.8552,61.5968,53.4419,80.7785c33.5869,19.1818,38.7986,37.9963,51.6138,52.8267
		c-3.4001-18.3276-24.2478-70.8237-63.3562-103.0742c-33.3735-27.5208-34.6194-90.6582-27.8032-118.2908
		C398.9855,501.4306,400.0644,536.2974,406.6083,563.7626z"
      />
    </g>
  </SvgIcon>
);