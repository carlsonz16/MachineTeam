import withMT from "@material-tailwind/react/utils/withMT";

export default withMT({
   content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}",
      ],
   theme: {
      extend: {
         fontFamily: {
         "FiraSans": ['Fira Sans', 'san-serif'],
         "Kanit": ['Kanit', 'san-serif'],
         "Tajawal": ['Tajawal', 'san-serif'],
         "Teko": ['Teko', 'san-serif'],
         "VarelaRound": ['Varela Round', 'san-serif'],
         "YanoneKaffeesatz": ['Yanone Kaffeesatz', 'san-serif'],
         "PTSans": ['PT Sans', 'sans-serif']
         }
      },
   },
   plugins: [],
});
