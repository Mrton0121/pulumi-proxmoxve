// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/muhlba91/pulumi-proxmoxve/sdk/v6/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

var _ = internal.GetEnvOrDefault

// The API token for the Proxmox VE API.
func GetApiToken(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:apiToken")
}

// The pre-authenticated Ticket for the Proxmox VE API.
func GetAuthTicket(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:authTicket")
}

// The pre-authenticated CSRF Prevention Token for the Proxmox VE API.
func GetCsrfPreventionToken(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:csrfPreventionToken")
}

// The endpoint for the Proxmox VE API.
func GetEndpoint(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:endpoint")
}

// Whether to skip the TLS verification step.
func GetInsecure(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "proxmoxve:insecure")
}

// The minimum required TLS version for API calls.Supported values: `1.0|1.1|1.2|1.3`. Defaults to `1.3`.
func GetMinTls(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:minTls")
}

// The one-time password for the Proxmox VE API.
//
// Deprecated: The `otp` attribute is deprecated and will be removed in a future release. Please use the `apiToken` attribute instead.
func GetOtp(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:otp")
}

// The password for the Proxmox VE API.
func GetPassword(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:password")
}

// The ending number for random VM / Container IDs.
func GetRandomVmIdEnd(ctx *pulumi.Context) int {
	return config.GetInt(ctx, "proxmoxve:randomVmIdEnd")
}

// The starting number for random VM / Container IDs.
func GetRandomVmIdStart(ctx *pulumi.Context) int {
	return config.GetInt(ctx, "proxmoxve:randomVmIdStart")
}

// Whether to generate random VM / Container IDs.
func GetRandomVmIds(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "proxmoxve:randomVmIds")
}

// The SSH configuration for the Proxmox nodes.
func GetSsh(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:ssh")
}

// The alternative temporary directory.
func GetTmpDir(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:tmpDir")
}

// The username for the Proxmox VE API.
func GetUsername(ctx *pulumi.Context) string {
	return config.Get(ctx, "proxmoxve:username")
}
