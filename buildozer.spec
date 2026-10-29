[app]

title = DJAMI SHOP
package.name = app
package.domain = com.djamishop

source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,kv,atlas,json
source.exclude_dirs = .git, .buildozer, bin, venv, .venv, __pycache__, vendor, web

version = 0.2
android.numeric_version = 2
icon.filename = %(source.dir)s/images/djami-shop-icon.png

requirements = python3==3.13.2,hostpython3==3.13.2,kivy==2.3.0,kivymd==2.0.0,materialyoucolor==3.0.3,materialshapes,asynckivy,asyncgui,pyjnius,certifi

orientation = portrait
fullscreen = 0

android.accept_sdk_license = True
android.api = 36
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a

android.permissions = INTERNET,ACCESS_NETWORK_STATE,POST_NOTIFICATIONS
android.enable_androidx = True
android.gradle_dependencies = com.google.firebase:firebase-messaging:24.1.2
android.add_src = %(source.dir)s/android_src
android.extra_manifest_application_xml = %(source.dir)s/android_src/firebase_manifest.xml
android.add_resources = %(source.dir)s/android_src/res

android.allow_backup = True
android.debug_artifact = apk
android.release_artifact = apk

p4a.url = https://github.com/kivy/python-for-android.git
p4a.branch = master
p4a.commit = 58d21141f17c889bf8585f5665921d72028f8831




[buildozer]

log_level = 2
warn_on_root = 1