import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        orka: {
          bg:      "#07070C",
          surface: "#0F0F1A",
          s2:      "#151526",
          border:  "#1E1E35",
          blue:    "#3B82F6",
          purple:  "#7C3AED",
          cyan:    "#06B6D4",
          text:    "#E8E8F0",
          muted:   "#6B6B8A",
        },
      },
    },
  },
  plugins: [],
};

export default config;
