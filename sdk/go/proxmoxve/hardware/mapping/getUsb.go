// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mapping

import (
	"context"
	"reflect"

	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves a USB hardware mapping from a Proxmox VE cluster.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/Hardware"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			example, err := Hardware.GetUsb(ctx, &mapping.GetUsbArgs{
//				Name: "example",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("dataProxmoxVirtualEnvironmentHardwareMappingUsb", example)
//			return nil
//		})
//	}
//
// ```
func LookupUsb(ctx *pulumi.Context, args *LookupUsbArgs, opts ...pulumi.InvokeOption) (*LookupUsbResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupUsbResult
	err := ctx.Invoke("proxmoxve:Hardware/mapping/getUsb:getUsb", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUsb.
type LookupUsbArgs struct {
	// The name of this USB hardware mapping.
	Name string `pulumi:"name"`
}

// A collection of values returned by getUsb.
type LookupUsbResult struct {
	// The comment of this USB hardware mapping.
	Comment string `pulumi:"comment"`
	// The unique identifier of this USB hardware mapping data source.
	Id string `pulumi:"id"`
	// The actual map of devices for the hardware mapping.
	Maps []GetUsbMap `pulumi:"maps"`
	// The name of this USB hardware mapping.
	Name string `pulumi:"name"`
}

func LookupUsbOutput(ctx *pulumi.Context, args LookupUsbOutputArgs, opts ...pulumi.InvokeOption) LookupUsbResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupUsbResultOutput, error) {
			args := v.(LookupUsbArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupUsbResult
			secret, err := ctx.InvokePackageRaw("proxmoxve:Hardware/mapping/getUsb:getUsb", args, &rv, "", opts...)
			if err != nil {
				return LookupUsbResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupUsbResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupUsbResultOutput), nil
			}
			return output, nil
		}).(LookupUsbResultOutput)
}

// A collection of arguments for invoking getUsb.
type LookupUsbOutputArgs struct {
	// The name of this USB hardware mapping.
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupUsbOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUsbArgs)(nil)).Elem()
}

// A collection of values returned by getUsb.
type LookupUsbResultOutput struct{ *pulumi.OutputState }

func (LookupUsbResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUsbResult)(nil)).Elem()
}

func (o LookupUsbResultOutput) ToLookupUsbResultOutput() LookupUsbResultOutput {
	return o
}

func (o LookupUsbResultOutput) ToLookupUsbResultOutputWithContext(ctx context.Context) LookupUsbResultOutput {
	return o
}

// The comment of this USB hardware mapping.
func (o LookupUsbResultOutput) Comment() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUsbResult) string { return v.Comment }).(pulumi.StringOutput)
}

// The unique identifier of this USB hardware mapping data source.
func (o LookupUsbResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUsbResult) string { return v.Id }).(pulumi.StringOutput)
}

// The actual map of devices for the hardware mapping.
func (o LookupUsbResultOutput) Maps() GetUsbMapArrayOutput {
	return o.ApplyT(func(v LookupUsbResult) []GetUsbMap { return v.Maps }).(GetUsbMapArrayOutput)
}

// The name of this USB hardware mapping.
func (o LookupUsbResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUsbResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupUsbResultOutput{})
}
