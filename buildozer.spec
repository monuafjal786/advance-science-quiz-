
[app]

title = Advance Science Centre Quiz
package.name = advancesciencequiz
package.domain = org.advancesciencecentre

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.archs = arm64-v8a

android.api = 35
android.minapi = 24
android.ndk = 28c
android.accept_sdk_license = True

p4a.bootstrap = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
