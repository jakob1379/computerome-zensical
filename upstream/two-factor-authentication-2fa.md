---
title: "Two Factor Authentication (2FA)"
description: "This guide provides instructions to install the required mobile app and use the privacyIDEA web interface to register/manage your tokens. Computerome requires two factor authentication for access in Computerome, no other software token is available for second factor authentication, other than the privacyIDEA app."
tags:
  - Security
  - Entrust Identity
  - Two Factor Authentication
  - Troubleshooting
  - Login
  - 2FA
  - privacyIDEA
---

# Two Factor Authentication (2FA)

![Screenshot](assets/uploads/privacy_IDEA_logo_6c94e0b139.png){ width="80" }

# How to set up privacyIDEA

This guide provides instructions to install the required mobile app and use the privacyIDEA web interface to register/manage your tokens.

:fontawesome-solid-circle-check: Step 1 Install App

:fontawesome-solid-circle-check: Step 2 Login to Web Interface

:fontawesome-solid-circle-check: Step 3 Enroll New Token

## Step 1 Install App

Install the official privacyIDEA authenticator app on your mobile phone:

[Download privacyIDEA for iOS :fontawesome-brands-apple:](https://apps.apple.com/us/app/privacyidea-authenticator/id1445401301)

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_02_ca831fed1f.png){ loading=lazy }

[Download privacyIDEA for Android :fontawesome-brands-android:](https://play.google.com/store/apps/details?id=it.netknights.piauthenticator)

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_01_d8250f7112.png){ loading=lazy }

## Step 2  Login to Web Interface

Open your browser and go to following URL and login using your username and password:

[https://pi.computerome.dk](https://pi.computerome.dk/)

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_03_d5ed6fb480.png){ loading=lazy }

## Step 3 Enroll New Token

After logging in, go to the "Tokens" section, and click on the "Enroll Token" from the left sidebar:

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_04_dbc2d48b61.png){ loading=lazy }

From the "Enroll a new token" list, you can choose **four token types**:

1. HOTP
2. TOTP
3. PUSH
4. SMS

**Note: We recommend that you create two tokens: one Push token as the primary token, and another token of type HOTP or TOTP as the secondary backup token.**
**When you're using a PUSH token along with other token types like HOTP or TOTP, the push token takes priority. In that case, you must approve the push notification on your phone to complete authentication.**

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_05_b48174cda3.png){ loading=lazy }

:fontawesome-solid-mobile-screen: Token Type 1

### HOTP (Event-based One-Time Password)

Generates a new OTP each time you manually tap the refresh button of token in the app.

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_06_98e0ccb837.png){ loading=lazy }

How to enroll a HOTP token:

1-1. Select HOTP from the list of token types:

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_07_9d61c31112.png){ loading=lazy }

1-2. Optionally, enter a description.

1-3. Leave the "PIN/Password" field empty.

1-4. Leave the "Assign the token to a container" field set to "No Container".

1-5. Click on "Enroll Token" button, a QR code will be generated and displayed on the screen:

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_08_de1c4c07c0.png){ loading=lazy }

1-6. Open the privacyIDEA authenticator app on your mobile device.

1-7.  Tap the QR code icon   and scan the QR code shown on the website. Once scanned, the token will be added to the app.

1-8. On the website, click the "Enroll a new token" button to confirm the enrollment.

1-9. From the left sidebar, click on "All Tokens" to view your token:

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_09_55c2f25f21.png){ loading=lazy }

1-10. Click on the token’s Serial Number (e.g., OATH00061722) to view token details and manage settings:

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_10_f148d9ec10.png){ loading=lazy }

1-11. Test the token. First generate a code (OTP) using the mobile app by tapping on the refresh button of the HOTP token, then on the token details page:

1.	Enter the code into the "Test token" field.
2.	Click on the "Test token" button.
3.	You will see the message "Successfully authenticated".  This confirms your token is working and ready for use.

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_11_18985beaf1.png){ loading=lazy }

:fontawesome-solid-mobile-screen: Token Type 2

### TOTP (Time-based One-Time Password)

Generates a 6-digit code that changes every 30 seconds.

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_12_c467909aee.png){ loading=lazy }

How to enroll a TOTP token:

Follow the same steps as described in the HOTP enrollment guide, with the exception that in Step 1.1, you must select TOTP as the token type instead of HOTP. All remaining steps including QR code scanning, token confirmation and testing, are exactly the same.

:fontawesome-solid-mobile-screen: Token Type 3 </

### PUSH token (Send a push notification to a smartphone)

Sends a push notification to your phone when you attempt to log in, and you can simply "Accept" or "Decline" the login request.

**NOTE** If you are already in the app before receiving the push notification, you must refresh the token list by pulling down on the app screen. This ensures the push notification is delivered to your device.

**NOTE** When using privacyIDEA, you will not receive a push notification on your phone during login. After entering your username and password for any Computerome service, you must manually open the privacyIDEA app on your phone to approve or deny the login request.

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_13_1037ccb01a.png){ loading=lazy }

How to enroll a PUSH token:

Follow the same steps as described in the HOTP enrollment guide, with the exception that in Step 1.1, you must select PUSH as the token type instead of HOTP and note that token testing is not applicable. All remaining steps are exactly the same.

:fontawesome-solid-mobile-screen: Token Type 4
**SMS token (Send a One Time Password to the users mobile phone)**

Sends a one-time password to your mobile phone via SMS during login.

How to enroll a SMS token:

4-1. Select SMS as the token type from the list:

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_14_2e0f5d7616.png){ loading=lazy }

4-2. Verify that the phone number displayed by the system is correct.

4-3. Optionally, enter a description in the "Description field".

4-4. Leave all other fields unchanged.

4-5. Click on the "Enroll Token" button.

4-6. Click on the "Enroll a new token" button.

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_15_0a67eac35e.png){ loading=lazy }

4-7. From the left sidebar, click "All Tokens" to view your token in the tokens list:

![Screenshot](assets/uploads/privacy_IDEA_2_FA_image_16_30d4a54308.png){ loading=lazy }
