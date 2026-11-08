[app]
title = DaleRun
package.name = dalerun
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.11.6,pygame==2.5.2,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf,png,jpeg
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a
p4a.branch = release-2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
