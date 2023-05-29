import {amber, grey} from '@mui/material/colors';
import { PaletteMode } from '@mui/material';

export const getTheme = (mode: PaletteMode) => ({
    palette: {
      mode,
      ...(mode === 'light'
        ? {
            // palette values for light mode
            primary: grey,
            divider: grey[500],
            background: {
                default: '#fff',
                paper: '#fff',
              },
            text: {
              primary: '#171F34',
              secondary: '#171F34',
            },
          }
        : {
            // palette values for dark mode
            primary: grey,
            divider: '#1d2846',
            background: {
              default: '#171F38',
              paper: '#171F35',
            },
            text: {
              primary: '#fff',
              secondary: grey[500],
            },
          }),
    },
});