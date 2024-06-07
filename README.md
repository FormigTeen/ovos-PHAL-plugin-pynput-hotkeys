## Pynput Hotkeys PHAL plugin

plugin for Keyboard hotkeys, define key combos to trigger bus events

## Install

`pip install git+https://github.com/FormigTeen/ovos-PHAL-plugin-pynput-hotkeys

## Configuration

Add any bus message + key combo under `"key_down"` and  `"key_up"`

```json
 "PHAL": {
    "ovos-PHAL-plugin-hotkeys": {
        "debug": false,
        "key_down": {
            "mycroft.mic.listen": "w",
            "mycroft.mic.mute.toggle": "i",
            "mycroft.mic.mute": "<shift>+m",
            "mycroft.mic.unmute": "<shift>+u",
            "mycroft.volume.increase": "u",
            "mycroft.volume.decrease": "g",
            "mycroft.volume.mute.toggle": "v",
            "mycroft.volume.mute": "<ctrl>+<shift>+m",
            "mycroft.volume.unmute": "<ctrl>+<shift>+u",
            "homescreen.manager.show_active": "v",
            "ovos.common_play.play_pause": "f"
       }
    }
}
```
