--- chrome/browser/resources/settings/appearance_page/appearance_page.ts.orig	2022-10-05 07:34:01 UTC
+++ chrome/browser/resources/settings/appearance_page/appearance_page.ts
@@ -145,7 +145,7 @@ export class SettingsAppearancePageElement extends
             'prefs.autogenerated.theme.policy.color.controlledBy)',
       },
 
-      // <if expr="is_linux">
+      // <if expr="is_posix">
       /**
        * Whether to show the "Custom Chrome Frame" setting.
        */
@@ -174,7 +174,7 @@ export class SettingsAppearancePageElement extends
       'themeChanged_(' +
           'prefs.extensions.theme.id.value, useSystemTheme_, isForcedTheme_)',
 
-      // <if expr="is_linux">
+      // <if expr="is_posix">
       // NOTE: this pref only exists on Linux.
       'useSystemThemePrefChanged_(prefs.extensions.theme.use_system.value)',
       // </if>
@@ -194,7 +194,7 @@ export class SettingsAppearancePageElement extends
   private showReaderModeOption_: boolean;
   private isForcedTheme_: boolean;
 
-  // <if expr="is_linux">
+  // <if expr="is_posix">
   private showCustomChromeFrame_: boolean;
   // </if>
 
@@ -272,7 +272,7 @@ export class SettingsAppearancePageElement extends
     this.appearanceBrowserProxy_.useDefaultTheme();
   }
 
-  // <if expr="is_linux">
+  // <if expr="is_posix">
   private useSystemThemePrefChanged_(useSystemTheme: boolean) {
     this.useSystemTheme_ = useSystemTheme;
   }
@@ -333,10 +333,10 @@ export class SettingsAppearancePageElement extends
     }
 
     let i18nId;
-    // <if expr="is_linux">
+    // <if expr="is_posix">
     i18nId = useSystemTheme ? 'systemTheme' : 'classicTheme';
     // </if>
-    // <if expr="not is_linux">
+    // <if expr="not is_posix">
     i18nId = 'chooseFromWebStore';
     // </if>
     this.themeSublabel_ = this.i18n(i18nId);
