# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import json
from ovos_bus_client.message import Message
from ovos_plugin_manager.phal import PHALPlugin
from ovos_utils.log import LOG
from pynput import keyboard



class HotKeysPlugin(PHALPlugin):
    """Keyboard hotkeys, define key combo to trigger listening"""

    def __init__(self, bus=None, config=None):
        print("Started Plugin")
        super().__init__(bus=bus, name="ovos-PHAL-plugin-hotkeys", config=config)
        self.register_callbacks()

    def register_callbacks(self):
        """combos are registered independently
        NOTE: same combo can only have 1 callback (up or down)"""
        print("This is a Configuration")
        print(self.config.get("key_down"))
        for msg_type, key in self.config.get("key_down", {}).items():
            if isinstance(key, int):
                continue

            def do_emit(k=key, m=msg_type):
                LOG.info(f"hotkey down {k} -> {m}")
                self.bus.emit(Message(m))

            listener = keyboard.GlobalHotKeys({key: do_emit})
            listener.start()

        for msg_type, key in self.config.get("key_up", {}).items():
            if isinstance(key, int):
                continue

            def do_emit(k=key, m=msg_type):
                LOG.info(f"hotkey up {k} -> {m}")
                self.bus.emit(Message(m))

            listener = keyboard.GlobalHotKeys({key: do_emit})
            listener.start()

    def run(self):
        self._running = True

        def on_press(key):
            try:
                scan_code = key.vk
            except AttributeError:
                scan_code = key.value.vk

            for msg_type, k in self.config.get("key_down", {}).items():
                if scan_code == k:
                    LOG.info(f"hotkey down {scan_code} -> {msg_type}")
                    self.bus.emit(Message(msg_type))

        def on_release(key):
            try:
                scan_code = key.vk
            except AttributeError:
                scan_code = key.value.vk

            for msg_type, k in self.config.get("key_up", {}).items():
                if scan_code == k:
                    LOG.info(f"hotkey up {scan_code} -> {msg_type}")
                    self.bus.emit(Message(msg_type))

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    def shutdown(self):
        super().shutdown()


if __name__ == "__main__":
    # debug
    from ovos_utils import wait_for_exit_signal
    from ovos_utils.messagebus import FakeBus

    p = HotKeysPlugin(FakeBus(), {"debug": True}
                      #            "key_down": {"test": 57, "test2": 28},
                      #            "key_up": {"test": 57, "test2": 28}}
                      )


    wait_for_exit_signal()