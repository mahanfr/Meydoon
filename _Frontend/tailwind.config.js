module.exports = {
  purge: [],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    extend: {
      colors:{
        brand:{
          background:{
            dark:'#050613',
            DEFAULT:'#F5F5F5',
          },
          card:{
            dark:'#0E1329',
            DEFAULT:'#E4E8F2',
          },
          gradientTop: '#4932C4',
          gradientBottom: '#4076E2',
          textColor1: '#EFEFEF',
          textColor2: '#D4D4D4',
          textColor3: '#343434',
          textColor4: '#707070',
        }
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
