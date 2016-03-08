#include "keymap_common.h"

const uint8_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /* 0: qwerty (mac) */
    KEYMAP(
        ESC,  1,    2,    3,    4,    5,    6,         7,    8,    9,    0,    MINS,  EQL,  BSPC, \
        GRV,  LBRC, Q,    W,    E,    R,    T,         Y,    U,    I,    O,    P,     RBRC, BSLS, \
        FN2,  TAB,  A,    S,    D,    F,    G,         H,    J,    K,    L,    SCLN,  QUOT, ENT, \
        FN1,  LSFT, Z,    X,    C,    V,    B,         N,    M,   COMM,  DOT,  SLSH,  RSFT, MUTE, \
        FN0,        LCTL, LALT, LGUI,       SPC,       SPC,       RGUI,  RALT, RCTL,        MEDIA_PLAY_PAUSE),
    /* 1 */
    KEYMAP(
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS, TRNS, TRNS, TRNS, TRNS,  TRNS, DEL, \
        TRNS, TRNS, TRNS, TRNS, UP,   TRNS, TRNS,      TRNS, TRNS, UP,   TRNS, TRNS,  TRNS, TRNS, \
        TRNS, TRNS, TRNS, LEFT, DOWN, RGHT, TRNS,      TRNS, LEFT, DOWN, RGHT, TRNS,  TRNS, TRNS, \
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS, TRNS, TRNS, TRNS, TRNS,  TRNS, TRNS, \
        TRNS,       TRNS, TRNS, TRNS,       TRNS,      TRNS,       TRNS, TRNS, TRNS,        TRNS),

    /* 2 */KEYMAP(
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS,    MS_ACCEL0, MS_ACCEL1, MS_ACCEL2, TRNS,     TRNS, TRNS, \
        TRNS, TRNS, TRNS, TRNS, UP,   TRNS, TRNS,      TRNS,    MS_BTN1,   MS_UP,     MS_BTN2,   TRNS,     TRNS, TRNS, \
        TRNS, TRNS, TRNS, LEFT, DOWN, RGHT, TRNS,      MS_BTN3, MS_LEFT,   MS_DOWN,   MS_RIGHT,  MS_BTN4,  TRNS, TRNS, \
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS,    TRNS,      TRNS,      TRNS,      TRNS,     TRNS, TRNS, \
        TRNS,       TRNS, TRNS, TRNS,       TRNS,      TRNS,               TRNS,      TRNS,      TRNS,           TRNS),
    /* 3 */
    KEYMAP(
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      FN3,  FN4,  TRNS, TRNS, TRNS,  TRNS, TRNS, \
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS, TRNS, TRNS, TRNS, TRNS,  TRNS, TRNS, \
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS, TRNS, TRNS, TRNS, TRNS,  TRNS, TRNS, \
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS, TRNS, TRNS, TRNS, TRNS,  TRNS, TRNS, \
        TRNS,       TRNS, TRNS, TRNS,       TRNS,      TRNS,       TRNS, TRNS, TRNS,        TRNS),
    /* 4 */
    KEYMAP(
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS, TRNS, TRNS, TRNS, TRNS,  TRNS, TRNS, \
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS, TRNS, TRNS, TRNS, TRNS,  TRNS, TRNS, \
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS, TRNS, TRNS, TRNS, TRNS,  TRNS, TRNS, \
        TRNS, TRNS, TRNS, TRNS, TRNS, TRNS, TRNS,      TRNS, TRNS, TRNS, TRNS, TRNS,  TRNS, TRNS, \
        TRNS,       LGUI, LALT, LCTL,       TRNS,      TRNS,       RCTL, RALT, RGUI,        TRNS),
};

const uint16_t PROGMEM fn_actions[] = {
  [0] = ACTION_LAYER_MOMENTARY(1), //arrow keys
  [1] = ACTION_LAYER_MOMENTARY(2), // mouse keys
  [2] = ACTION_LAYER_MOMENTARY(3), // layer switcher
  [3] = ACTION_DEFAULT_LAYER_SET(0), // mac qwerty
  [4] = ACTION_DEFAULT_LAYER_SET(4), // hacked linux/windows super key switch
};
