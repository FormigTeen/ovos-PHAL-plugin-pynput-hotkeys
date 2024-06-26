#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'ovos-PHAL-plugin-pynput-hotkeys=ovos_phal_plugin_pynput_hotkeys:HotKeysPlugin'
setup(
    name='ovos-PHAL-plugin-pynput-hotkeys',
    version='0.0.1',
    description='map keypresses to OVOS bus events',
    url='https://github.com/FormigTeen/ovos-PHAL-plugin-pynput-hotkeys',
    author='FormigTeen',
    author_email='msformigteen@live.com',
    license='Apache-2.0',
    packages=['ovos_phal_plugin_pynput_hotkeys'],
    install_requires=["ovos-plugin-manager"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='OVOS plugin',
    entry_points={'ovos.plugin.phal': PLUGIN_ENTRY_POINT}
)
