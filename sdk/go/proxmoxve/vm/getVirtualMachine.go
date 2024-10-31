// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vm

import (
	"context"
	"reflect"

	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves information about a specific VM.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/VM"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := VM.GetVirtualMachine(ctx, &vm.GetVirtualMachineArgs{
//				NodeName: "test",
//				VmId:     100,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupVirtualMachine(ctx *pulumi.Context, args *LookupVirtualMachineArgs, opts ...pulumi.InvokeOption) (*LookupVirtualMachineResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVirtualMachineResult
	err := ctx.Invoke("proxmoxve:VM/getVirtualMachine:getVirtualMachine", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVirtualMachine.
type LookupVirtualMachineArgs struct {
	// The node name.
	NodeName string `pulumi:"nodeName"`
	// Status of the VM
	Status *string `pulumi:"status"`
	// Is VM a template (true) or a regular VM (false)
	Template *bool `pulumi:"template"`
	// The VM identifier.
	VmId int `pulumi:"vmId"`
}

// A collection of values returned by getVirtualMachine.
type LookupVirtualMachineResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The virtual machine name.
	Name     string `pulumi:"name"`
	NodeName string `pulumi:"nodeName"`
	// Status of the VM
	Status *string `pulumi:"status"`
	// A list of tags of the VM.
	Tags []string `pulumi:"tags"`
	// Is VM a template (true) or a regular VM (false)
	Template *bool `pulumi:"template"`
	VmId     int   `pulumi:"vmId"`
}

func LookupVirtualMachineOutput(ctx *pulumi.Context, args LookupVirtualMachineOutputArgs, opts ...pulumi.InvokeOption) LookupVirtualMachineResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVirtualMachineResultOutput, error) {
			args := v.(LookupVirtualMachineArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupVirtualMachineResult
			secret, err := ctx.InvokePackageRaw("proxmoxve:VM/getVirtualMachine:getVirtualMachine", args, &rv, "", opts...)
			if err != nil {
				return LookupVirtualMachineResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupVirtualMachineResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupVirtualMachineResultOutput), nil
			}
			return output, nil
		}).(LookupVirtualMachineResultOutput)
}

// A collection of arguments for invoking getVirtualMachine.
type LookupVirtualMachineOutputArgs struct {
	// The node name.
	NodeName pulumi.StringInput `pulumi:"nodeName"`
	// Status of the VM
	Status pulumi.StringPtrInput `pulumi:"status"`
	// Is VM a template (true) or a regular VM (false)
	Template pulumi.BoolPtrInput `pulumi:"template"`
	// The VM identifier.
	VmId pulumi.IntInput `pulumi:"vmId"`
}

func (LookupVirtualMachineOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVirtualMachineArgs)(nil)).Elem()
}

// A collection of values returned by getVirtualMachine.
type LookupVirtualMachineResultOutput struct{ *pulumi.OutputState }

func (LookupVirtualMachineResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVirtualMachineResult)(nil)).Elem()
}

func (o LookupVirtualMachineResultOutput) ToLookupVirtualMachineResultOutput() LookupVirtualMachineResultOutput {
	return o
}

func (o LookupVirtualMachineResultOutput) ToLookupVirtualMachineResultOutputWithContext(ctx context.Context) LookupVirtualMachineResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o LookupVirtualMachineResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVirtualMachineResult) string { return v.Id }).(pulumi.StringOutput)
}

// The virtual machine name.
func (o LookupVirtualMachineResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVirtualMachineResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupVirtualMachineResultOutput) NodeName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVirtualMachineResult) string { return v.NodeName }).(pulumi.StringOutput)
}

// Status of the VM
func (o LookupVirtualMachineResultOutput) Status() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVirtualMachineResult) *string { return v.Status }).(pulumi.StringPtrOutput)
}

// A list of tags of the VM.
func (o LookupVirtualMachineResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupVirtualMachineResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// Is VM a template (true) or a regular VM (false)
func (o LookupVirtualMachineResultOutput) Template() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupVirtualMachineResult) *bool { return v.Template }).(pulumi.BoolPtrOutput)
}

func (o LookupVirtualMachineResultOutput) VmId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupVirtualMachineResult) int { return v.VmId }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVirtualMachineResultOutput{})
}
