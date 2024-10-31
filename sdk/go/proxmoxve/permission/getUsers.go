// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package permission

import (
	"context"
	"reflect"

	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves information about all the available users.
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
//			_, err := Permission.GetUsers(ctx, map[string]interface{}{}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetUsers(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetUsersResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetUsersResult
	err := ctx.Invoke("proxmoxve:Permission/getUsers:getUsers", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getUsers.
type GetUsersResult struct {
	// The user comments.
	Comments []string `pulumi:"comments"`
	// The users' email addresses.
	Emails []string `pulumi:"emails"`
	// Whether a user account is enabled.
	Enableds []bool `pulumi:"enableds"`
	// The user accounts' expiration dates (RFC 3339).
	ExpirationDates []string `pulumi:"expirationDates"`
	// The users' first names.
	FirstNames []string `pulumi:"firstNames"`
	// The users' groups.
	Groups [][]string `pulumi:"groups"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The users' keys.
	Keys []string `pulumi:"keys"`
	// The users' last names.
	LastNames []string `pulumi:"lastNames"`
	// The user identifiers.
	UserIds []string `pulumi:"userIds"`
}

func GetUsersOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetUsersResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetUsersResultOutput, error) {
		opts = internal.PkgInvokeDefaultOpts(opts)
		var rv GetUsersResult
		secret, err := ctx.InvokePackageRaw("proxmoxve:Permission/getUsers:getUsers", nil, &rv, "", opts...)
		if err != nil {
			return GetUsersResultOutput{}, err
		}

		output := pulumi.ToOutput(rv).(GetUsersResultOutput)
		if secret {
			return pulumi.ToSecret(output).(GetUsersResultOutput), nil
		}
		return output, nil
	}).(GetUsersResultOutput)
}

// A collection of values returned by getUsers.
type GetUsersResultOutput struct{ *pulumi.OutputState }

func (GetUsersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUsersResult)(nil)).Elem()
}

func (o GetUsersResultOutput) ToGetUsersResultOutput() GetUsersResultOutput {
	return o
}

func (o GetUsersResultOutput) ToGetUsersResultOutputWithContext(ctx context.Context) GetUsersResultOutput {
	return o
}

// The user comments.
func (o GetUsersResultOutput) Comments() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetUsersResult) []string { return v.Comments }).(pulumi.StringArrayOutput)
}

// The users' email addresses.
func (o GetUsersResultOutput) Emails() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetUsersResult) []string { return v.Emails }).(pulumi.StringArrayOutput)
}

// Whether a user account is enabled.
func (o GetUsersResultOutput) Enableds() pulumi.BoolArrayOutput {
	return o.ApplyT(func(v GetUsersResult) []bool { return v.Enableds }).(pulumi.BoolArrayOutput)
}

// The user accounts' expiration dates (RFC 3339).
func (o GetUsersResultOutput) ExpirationDates() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetUsersResult) []string { return v.ExpirationDates }).(pulumi.StringArrayOutput)
}

// The users' first names.
func (o GetUsersResultOutput) FirstNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetUsersResult) []string { return v.FirstNames }).(pulumi.StringArrayOutput)
}

// The users' groups.
func (o GetUsersResultOutput) Groups() pulumi.StringArrayArrayOutput {
	return o.ApplyT(func(v GetUsersResult) [][]string { return v.Groups }).(pulumi.StringArrayArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetUsersResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetUsersResult) string { return v.Id }).(pulumi.StringOutput)
}

// The users' keys.
func (o GetUsersResultOutput) Keys() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetUsersResult) []string { return v.Keys }).(pulumi.StringArrayOutput)
}

// The users' last names.
func (o GetUsersResultOutput) LastNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetUsersResult) []string { return v.LastNames }).(pulumi.StringArrayOutput)
}

// The user identifiers.
func (o GetUsersResultOutput) UserIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetUsersResult) []string { return v.UserIds }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetUsersResultOutput{})
}
