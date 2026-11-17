---
title: "IP Restrictions"
description: "To enhance security, Computerome restricts access to its services to users connecting from Danish IP addresses or from IP addresses that have been explicitly approved."
icon: lucide/globe-lock
---

# IP Restrictions

To enhance security, Computerome restricts access to its services to users connecting from Danish IP addresses or from IP addresses that have been explicitly approved.

This restriction applies to:

- HPC services
- Cloud services
- Other shared Computerome services

!!! note

    This restriction does not affect direct access to your own Cloud VM if it has been assigned a public IP address.

## Access via organizational VPN

If your organization provides a VPN service, we recommend using it when accessing Computerome services. In many cases, access can be granted by whitelisting your organization's public IP range, allowing all users connected through the VPN to access the services without requiring individual IP whitelist requests.

## Requesting IP whitelisting

If you need access from a non-Danish or otherwise restricted network, you can request that your IP address be whitelisted.

!!! tip

    You might also add the public IP address of your phone, as it is needed for MFA.

### Self-service

Visit [https://verify.computerome.dk](https://verify.computerome.dk) from a blocked IP address and complete the security verification. If successful, your current public IP will then be collected and added to the firewall whitelist automatically within a few minutes.

### Manual process

If the self-service is not working or not applicable to you, please reach out to us directly.

1. Determine your public IP address using a service such as [https://ifconfig.me/ip](https://ifconfig.me/ip).
2. Send an email to [**computerome@dtu.dk**](mailto:computerome@dtu.dk) containing:
    - Your public IP address
    - Your organization name (if applicable)
    - The service you need access to

Once your request has been processed, you should be able to access the restricted Computerome services from the approved IP address.
