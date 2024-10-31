// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"context"
	"reflect"

	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves all the host entries from a specific node.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/Network"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Network.GetHosts(ctx, &network.GetHostsArgs{
//				NodeName: "first-node",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetHosts(ctx *pulumi.Context, args *GetHostsArgs, opts ...pulumi.InvokeOption) (*GetHostsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetHostsResult
	err := ctx.Invoke("proxmoxve:Network/getHosts:getHosts", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getHosts.
type GetHostsArgs struct {
	// A node name.
	NodeName string `pulumi:"nodeName"`
}

// A collection of values returned by getHosts.
type GetHostsResult struct {
	// The IP addresses.
	Addresses []string `pulumi:"addresses"`
	// The SHA1 digest.
	Digest string `pulumi:"digest"`
	// The host entries (conversion of `addresses` and `hostnames` into
	// objects).
	Entries []GetHostsEntry `pulumi:"entries"`
	// The hostnames associated with each of the IP addresses.
	Hostnames [][]string `pulumi:"hostnames"`
	// The provider-assigned unique ID for this managed resource.
	Id       string `pulumi:"id"`
	NodeName string `pulumi:"nodeName"`
}

func GetHostsOutput(ctx *pulumi.Context, args GetHostsOutputArgs, opts ...pulumi.InvokeOption) GetHostsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetHostsResultOutput, error) {
			args := v.(GetHostsArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetHostsResult
			secret, err := ctx.InvokePackageRaw("proxmoxve:Network/getHosts:getHosts", args, &rv, "", opts...)
			if err != nil {
				return GetHostsResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetHostsResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetHostsResultOutput), nil
			}
			return output, nil
		}).(GetHostsResultOutput)
}

// A collection of arguments for invoking getHosts.
type GetHostsOutputArgs struct {
	// A node name.
	NodeName pulumi.StringInput `pulumi:"nodeName"`
}

func (GetHostsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetHostsArgs)(nil)).Elem()
}

// A collection of values returned by getHosts.
type GetHostsResultOutput struct{ *pulumi.OutputState }

func (GetHostsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetHostsResult)(nil)).Elem()
}

func (o GetHostsResultOutput) ToGetHostsResultOutput() GetHostsResultOutput {
	return o
}

func (o GetHostsResultOutput) ToGetHostsResultOutputWithContext(ctx context.Context) GetHostsResultOutput {
	return o
}

// The IP addresses.
func (o GetHostsResultOutput) Addresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetHostsResult) []string { return v.Addresses }).(pulumi.StringArrayOutput)
}

// The SHA1 digest.
func (o GetHostsResultOutput) Digest() pulumi.StringOutput {
	return o.ApplyT(func(v GetHostsResult) string { return v.Digest }).(pulumi.StringOutput)
}

// The host entries (conversion of `addresses` and `hostnames` into
// objects).
func (o GetHostsResultOutput) Entries() GetHostsEntryArrayOutput {
	return o.ApplyT(func(v GetHostsResult) []GetHostsEntry { return v.Entries }).(GetHostsEntryArrayOutput)
}

// The hostnames associated with each of the IP addresses.
func (o GetHostsResultOutput) Hostnames() pulumi.StringArrayArrayOutput {
	return o.ApplyT(func(v GetHostsResult) [][]string { return v.Hostnames }).(pulumi.StringArrayArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetHostsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetHostsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetHostsResultOutput) NodeName() pulumi.StringOutput {
	return o.ApplyT(func(v GetHostsResult) string { return v.NodeName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetHostsResultOutput{})
}
