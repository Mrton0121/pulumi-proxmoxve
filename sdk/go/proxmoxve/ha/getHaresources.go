// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ha

import (
	"context"
	"reflect"

	"github.com/muhlba91/pulumi-proxmoxve/sdk/v5/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves the list of High Availability resources.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/muhlba91/pulumi-proxmoxve/sdk/v5/go/proxmoxve/HA"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			exampleAll, err := HA.GetHAResources(ctx, nil, nil)
//			if err != nil {
//				return err
//			}
//			exampleVm, err := HA.GetHAResources(ctx, &ha.GetHAResourcesArgs{
//				Type: pulumi.StringRef("vm"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("dataProxmoxVirtualEnvironmentHaresources", map[string]interface{}{
//				"all": exampleAll.ResourceIds,
//				"vms": exampleVm.ResourceIds,
//			})
//			return nil
//		})
//	}
//
// ```
func GetHAResources(ctx *pulumi.Context, args *GetHAResourcesArgs, opts ...pulumi.InvokeOption) (*GetHAResourcesResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetHAResourcesResult
	err := ctx.Invoke("proxmoxve:HA/getHAResources:getHAResources", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getHAResources.
type GetHAResourcesArgs struct {
	// The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
	Type *string `pulumi:"type"`
}

// A collection of values returned by getHAResources.
type GetHAResourcesResult struct {
	// The unique identifier of this resource.
	Id string `pulumi:"id"`
	// The identifiers of the High Availability resources.
	ResourceIds []string `pulumi:"resourceIds"`
	// The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
	Type *string `pulumi:"type"`
}

func GetHAResourcesOutput(ctx *pulumi.Context, args GetHAResourcesOutputArgs, opts ...pulumi.InvokeOption) GetHAResourcesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetHAResourcesResult, error) {
			args := v.(GetHAResourcesArgs)
			r, err := GetHAResources(ctx, &args, opts...)
			var s GetHAResourcesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetHAResourcesResultOutput)
}

// A collection of arguments for invoking getHAResources.
type GetHAResourcesOutputArgs struct {
	// The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
	Type pulumi.StringPtrInput `pulumi:"type"`
}

func (GetHAResourcesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetHAResourcesArgs)(nil)).Elem()
}

// A collection of values returned by getHAResources.
type GetHAResourcesResultOutput struct{ *pulumi.OutputState }

func (GetHAResourcesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetHAResourcesResult)(nil)).Elem()
}

func (o GetHAResourcesResultOutput) ToGetHAResourcesResultOutput() GetHAResourcesResultOutput {
	return o
}

func (o GetHAResourcesResultOutput) ToGetHAResourcesResultOutputWithContext(ctx context.Context) GetHAResourcesResultOutput {
	return o
}

// The unique identifier of this resource.
func (o GetHAResourcesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetHAResourcesResult) string { return v.Id }).(pulumi.StringOutput)
}

// The identifiers of the High Availability resources.
func (o GetHAResourcesResultOutput) ResourceIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetHAResourcesResult) []string { return v.ResourceIds }).(pulumi.StringArrayOutput)
}

// The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
func (o GetHAResourcesResultOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetHAResourcesResult) *string { return v.Type }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetHAResourcesResultOutput{})
}
