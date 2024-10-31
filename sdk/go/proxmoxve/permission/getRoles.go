// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package permission

import (
	"context"
	"reflect"

	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves information about all the available roles.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/Permission"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Permission.GetRoles(ctx, map[string]interface{}{}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetRoles(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetRolesResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetRolesResult
	err := ctx.Invoke("proxmoxve:Permission/getRoles:getRoles", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getRoles.
type GetRolesResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The role privileges.
	Privileges [][]string `pulumi:"privileges"`
	// The role identifiers.
	RoleIds []string `pulumi:"roleIds"`
	// Whether the role is special (built-in).
	Specials []bool `pulumi:"specials"`
}

func GetRolesOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetRolesResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetRolesResultOutput, error) {
		opts = internal.PkgInvokeDefaultOpts(opts)
		var rv GetRolesResult
		secret, err := ctx.InvokePackageRaw("proxmoxve:Permission/getRoles:getRoles", nil, &rv, "", opts...)
		if err != nil {
			return GetRolesResultOutput{}, err
		}

		output := pulumi.ToOutput(rv).(GetRolesResultOutput)
		if secret {
			return pulumi.ToSecret(output).(GetRolesResultOutput), nil
		}
		return output, nil
	}).(GetRolesResultOutput)
}

// A collection of values returned by getRoles.
type GetRolesResultOutput struct{ *pulumi.OutputState }

func (GetRolesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRolesResult)(nil)).Elem()
}

func (o GetRolesResultOutput) ToGetRolesResultOutput() GetRolesResultOutput {
	return o
}

func (o GetRolesResultOutput) ToGetRolesResultOutputWithContext(ctx context.Context) GetRolesResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetRolesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetRolesResult) string { return v.Id }).(pulumi.StringOutput)
}

// The role privileges.
func (o GetRolesResultOutput) Privileges() pulumi.StringArrayArrayOutput {
	return o.ApplyT(func(v GetRolesResult) [][]string { return v.Privileges }).(pulumi.StringArrayArrayOutput)
}

// The role identifiers.
func (o GetRolesResultOutput) RoleIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetRolesResult) []string { return v.RoleIds }).(pulumi.StringArrayOutput)
}

// Whether the role is special (built-in).
func (o GetRolesResultOutput) Specials() pulumi.BoolArrayOutput {
	return o.ApplyT(func(v GetRolesResult) []bool { return v.Specials }).(pulumi.BoolArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetRolesResultOutput{})
}
