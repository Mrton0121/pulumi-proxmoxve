// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package acme

import (
	"context"
	"reflect"

	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves the list of ACME plugins.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/Acme"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			example, err := Acme.GetPlugins(ctx, map[string]interface{}{}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("dataProxmoxVirtualEnvironmentAcmePlugins", example.Plugins)
//			return nil
//		})
//	}
//
// ```
func GetPlugins(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetPluginsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetPluginsResult
	err := ctx.Invoke("proxmoxve:Acme/getPlugins:getPlugins", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getPlugins.
type GetPluginsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// List of ACME plugins
	Plugins []GetPluginsPlugin `pulumi:"plugins"`
}

func GetPluginsOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetPluginsResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetPluginsResultOutput, error) {
		opts = internal.PkgInvokeDefaultOpts(opts)
		var rv GetPluginsResult
		secret, err := ctx.InvokePackageRaw("proxmoxve:Acme/getPlugins:getPlugins", nil, &rv, "", opts...)
		if err != nil {
			return GetPluginsResultOutput{}, err
		}

		output := pulumi.ToOutput(rv).(GetPluginsResultOutput)
		if secret {
			return pulumi.ToSecret(output).(GetPluginsResultOutput), nil
		}
		return output, nil
	}).(GetPluginsResultOutput)
}

// A collection of values returned by getPlugins.
type GetPluginsResultOutput struct{ *pulumi.OutputState }

func (GetPluginsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPluginsResult)(nil)).Elem()
}

func (o GetPluginsResultOutput) ToGetPluginsResultOutput() GetPluginsResultOutput {
	return o
}

func (o GetPluginsResultOutput) ToGetPluginsResultOutputWithContext(ctx context.Context) GetPluginsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetPluginsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetPluginsResult) string { return v.Id }).(pulumi.StringOutput)
}

// List of ACME plugins
func (o GetPluginsResultOutput) Plugins() GetPluginsPluginArrayOutput {
	return o.ApplyT(func(v GetPluginsResult) []GetPluginsPlugin { return v.Plugins }).(GetPluginsPluginArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPluginsResultOutput{})
}
