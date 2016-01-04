#include "keymap_common.h"

const uint8_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /* 0: qwerty */
    KEYMAP(
        ESC,  1,    2,    3,    4,    5,   6,         7,   8,    9,   0,    MINS,  EQL,  BSPC, \
        GRV,  LBRC, Q,    W,    E,    R,   T,         Y,   U,    I,   O,    P,     RBRC, BSLS, \
        F2,   TAB,  A,    S,    D,    F,   G,         H,   J,    K,   L,    SCLN,  QUOT, ENT, \
        F3,   LSFT, Z,    X,    C,    V,   B,         N,   M,   COMM, DOT,  SLSH,  RSFT, F4, \
        LCTL,       LGUI, LALT, FN0,       SPC,       SPC,      FN1,  RALT, RGUI,         RCTL)
};
const uint16_t PROGMEM fn_actions[] = {
    //[0] = ACTION_MODS_KEY(MOD_RCTL|MOD_RSFT, KC_ESC), // Task(RControl,RShift+Esc)
    //[0] = ACTION_DEFAULT_LAYER_SET(0)  // set qwerty layout
};
