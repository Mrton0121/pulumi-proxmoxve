// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ha

import (
	"context"
	"reflect"

	"errors"
	"github.com/muhlba91/pulumi-proxmoxve/sdk/v5/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages Proxmox HA resources.
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
//			_, err := HA.NewHAResource(ctx, "example", &HA.HAResourceArgs{
//				ResourceId: pulumi.String("vm:123"),
//				State:      pulumi.String("started"),
//				Group:      pulumi.String("example"),
//				Comment:    pulumi.String("Managed by Terraform"),
//			}, pulumi.DependsOn([]pulumi.Resource{
//				proxmox_virtual_environment_hagroup.Example,
//			}))
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// #!/usr/bin/env sh
//
//	HA resources can be imported using their identifiers, e.g.:
//
// ```sh
// $ pulumi import proxmoxve:HA/hAResource:HAResource example vm:123
// ```
type HAResource struct {
	pulumi.CustomResourceState

	// The comment associated with this resource.
	Comment pulumi.StringPtrOutput `pulumi:"comment"`
	// The identifier of the High Availability group this resource is a member of.
	Group pulumi.StringPtrOutput `pulumi:"group"`
	// The maximal number of relocation attempts.
	MaxRelocate pulumi.IntPtrOutput `pulumi:"maxRelocate"`
	// The maximal number of restart attempts.
	MaxRestart pulumi.IntPtrOutput `pulumi:"maxRestart"`
	// The Proxmox HA resource identifier
	ResourceId pulumi.StringOutput `pulumi:"resourceId"`
	// The desired state of the resource.
	State pulumi.StringOutput `pulumi:"state"`
	// The type of HA resources to create. If unset, it will be deduced from the `resourceId`.
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewHAResource registers a new resource with the given unique name, arguments, and options.
func NewHAResource(ctx *pulumi.Context,
	name string, args *HAResourceArgs, opts ...pulumi.ResourceOption) (*HAResource, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ResourceId == nil {
		return nil, errors.New("invalid value for required argument 'ResourceId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource HAResource
	err := ctx.RegisterResource("proxmoxve:HA/hAResource:HAResource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHAResource gets an existing HAResource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHAResource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HAResourceState, opts ...pulumi.ResourceOption) (*HAResource, error) {
	var resource HAResource
	err := ctx.ReadResource("proxmoxve:HA/hAResource:HAResource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HAResource resources.
type haresourceState struct {
	// The comment associated with this resource.
	Comment *string `pulumi:"comment"`
	// The identifier of the High Availability group this resource is a member of.
	Group *string `pulumi:"group"`
	// The maximal number of relocation attempts.
	MaxRelocate *int `pulumi:"maxRelocate"`
	// The maximal number of restart attempts.
	MaxRestart *int `pulumi:"maxRestart"`
	// The Proxmox HA resource identifier
	ResourceId *string `pulumi:"resourceId"`
	// The desired state of the resource.
	State *string `pulumi:"state"`
	// The type of HA resources to create. If unset, it will be deduced from the `resourceId`.
	Type *string `pulumi:"type"`
}

type HAResourceState struct {
	// The comment associated with this resource.
	Comment pulumi.StringPtrInput
	// The identifier of the High Availability group this resource is a member of.
	Group pulumi.StringPtrInput
	// The maximal number of relocation attempts.
	MaxRelocate pulumi.IntPtrInput
	// The maximal number of restart attempts.
	MaxRestart pulumi.IntPtrInput
	// The Proxmox HA resource identifier
	ResourceId pulumi.StringPtrInput
	// The desired state of the resource.
	State pulumi.StringPtrInput
	// The type of HA resources to create. If unset, it will be deduced from the `resourceId`.
	Type pulumi.StringPtrInput
}

func (HAResourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*haresourceState)(nil)).Elem()
}

type haresourceArgs struct {
	// The comment associated with this resource.
	Comment *string `pulumi:"comment"`
	// The identifier of the High Availability group this resource is a member of.
	Group *string `pulumi:"group"`
	// The maximal number of relocation attempts.
	MaxRelocate *int `pulumi:"maxRelocate"`
	// The maximal number of restart attempts.
	MaxRestart *int `pulumi:"maxRestart"`
	// The Proxmox HA resource identifier
	ResourceId string `pulumi:"resourceId"`
	// The desired state of the resource.
	State *string `pulumi:"state"`
	// The type of HA resources to create. If unset, it will be deduced from the `resourceId`.
	Type *string `pulumi:"type"`
}

// The set of arguments for constructing a HAResource resource.
type HAResourceArgs struct {
	// The comment associated with this resource.
	Comment pulumi.StringPtrInput
	// The identifier of the High Availability group this resource is a member of.
	Group pulumi.StringPtrInput
	// The maximal number of relocation attempts.
	MaxRelocate pulumi.IntPtrInput
	// The maximal number of restart attempts.
	MaxRestart pulumi.IntPtrInput
	// The Proxmox HA resource identifier
	ResourceId pulumi.StringInput
	// The desired state of the resource.
	State pulumi.StringPtrInput
	// The type of HA resources to create. If unset, it will be deduced from the `resourceId`.
	Type pulumi.StringPtrInput
}

func (HAResourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*haresourceArgs)(nil)).Elem()
}

type HAResourceInput interface {
	pulumi.Input

	ToHAResourceOutput() HAResourceOutput
	ToHAResourceOutputWithContext(ctx context.Context) HAResourceOutput
}

func (*HAResource) ElementType() reflect.Type {
	return reflect.TypeOf((**HAResource)(nil)).Elem()
}

func (i *HAResource) ToHAResourceOutput() HAResourceOutput {
	return i.ToHAResourceOutputWithContext(context.Background())
}

func (i *HAResource) ToHAResourceOutputWithContext(ctx context.Context) HAResourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HAResourceOutput)
}

// HAResourceArrayInput is an input type that accepts HAResourceArray and HAResourceArrayOutput values.
// You can construct a concrete instance of `HAResourceArrayInput` via:
//
//	HAResourceArray{ HAResourceArgs{...} }
type HAResourceArrayInput interface {
	pulumi.Input

	ToHAResourceArrayOutput() HAResourceArrayOutput
	ToHAResourceArrayOutputWithContext(context.Context) HAResourceArrayOutput
}

type HAResourceArray []HAResourceInput

func (HAResourceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*HAResource)(nil)).Elem()
}

func (i HAResourceArray) ToHAResourceArrayOutput() HAResourceArrayOutput {
	return i.ToHAResourceArrayOutputWithContext(context.Background())
}

func (i HAResourceArray) ToHAResourceArrayOutputWithContext(ctx context.Context) HAResourceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HAResourceArrayOutput)
}

// HAResourceMapInput is an input type that accepts HAResourceMap and HAResourceMapOutput values.
// You can construct a concrete instance of `HAResourceMapInput` via:
//
//	HAResourceMap{ "key": HAResourceArgs{...} }
type HAResourceMapInput interface {
	pulumi.Input

	ToHAResourceMapOutput() HAResourceMapOutput
	ToHAResourceMapOutputWithContext(context.Context) HAResourceMapOutput
}

type HAResourceMap map[string]HAResourceInput

func (HAResourceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*HAResource)(nil)).Elem()
}

func (i HAResourceMap) ToHAResourceMapOutput() HAResourceMapOutput {
	return i.ToHAResourceMapOutputWithContext(context.Background())
}

func (i HAResourceMap) ToHAResourceMapOutputWithContext(ctx context.Context) HAResourceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HAResourceMapOutput)
}

type HAResourceOutput struct{ *pulumi.OutputState }

func (HAResourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**HAResource)(nil)).Elem()
}

func (o HAResourceOutput) ToHAResourceOutput() HAResourceOutput {
	return o
}

func (o HAResourceOutput) ToHAResourceOutputWithContext(ctx context.Context) HAResourceOutput {
	return o
}

// The comment associated with this resource.
func (o HAResourceOutput) Comment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *HAResource) pulumi.StringPtrOutput { return v.Comment }).(pulumi.StringPtrOutput)
}

// The identifier of the High Availability group this resource is a member of.
func (o HAResourceOutput) Group() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *HAResource) pulumi.StringPtrOutput { return v.Group }).(pulumi.StringPtrOutput)
}

// The maximal number of relocation attempts.
func (o HAResourceOutput) MaxRelocate() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *HAResource) pulumi.IntPtrOutput { return v.MaxRelocate }).(pulumi.IntPtrOutput)
}

// The maximal number of restart attempts.
func (o HAResourceOutput) MaxRestart() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *HAResource) pulumi.IntPtrOutput { return v.MaxRestart }).(pulumi.IntPtrOutput)
}

// The Proxmox HA resource identifier
func (o HAResourceOutput) ResourceId() pulumi.StringOutput {
	return o.ApplyT(func(v *HAResource) pulumi.StringOutput { return v.ResourceId }).(pulumi.StringOutput)
}

// The desired state of the resource.
func (o HAResourceOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *HAResource) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// The type of HA resources to create. If unset, it will be deduced from the `resourceId`.
func (o HAResourceOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *HAResource) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

type HAResourceArrayOutput struct{ *pulumi.OutputState }

func (HAResourceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*HAResource)(nil)).Elem()
}

func (o HAResourceArrayOutput) ToHAResourceArrayOutput() HAResourceArrayOutput {
	return o
}

func (o HAResourceArrayOutput) ToHAResourceArrayOutputWithContext(ctx context.Context) HAResourceArrayOutput {
	return o
}

func (o HAResourceArrayOutput) Index(i pulumi.IntInput) HAResourceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *HAResource {
		return vs[0].([]*HAResource)[vs[1].(int)]
	}).(HAResourceOutput)
}

type HAResourceMapOutput struct{ *pulumi.OutputState }

func (HAResourceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*HAResource)(nil)).Elem()
}

func (o HAResourceMapOutput) ToHAResourceMapOutput() HAResourceMapOutput {
	return o
}

func (o HAResourceMapOutput) ToHAResourceMapOutputWithContext(ctx context.Context) HAResourceMapOutput {
	return o
}

func (o HAResourceMapOutput) MapIndex(k pulumi.StringInput) HAResourceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *HAResource {
		return vs[0].(map[string]*HAResource)[vs[1].(string)]
	}).(HAResourceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*HAResourceInput)(nil)).Elem(), &HAResource{})
	pulumi.RegisterInputType(reflect.TypeOf((*HAResourceArrayInput)(nil)).Elem(), HAResourceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*HAResourceMapInput)(nil)).Elem(), HAResourceMap{})
	pulumi.RegisterOutputType(HAResourceOutput{})
	pulumi.RegisterOutputType(HAResourceArrayOutput{})
	pulumi.RegisterOutputType(HAResourceMapOutput{})
}