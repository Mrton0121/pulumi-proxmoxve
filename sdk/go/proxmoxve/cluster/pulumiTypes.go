// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cluster

import (
	"context"
	"reflect"

	"github.com/muhlba91/pulumi-proxmoxve/sdk/v6/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type OptionsNextId struct {
	// The minimum number for the next free VM ID. Must be higher or equal to 100
	Lower *int `pulumi:"lower"`
	// The maximum number for the next free VM ID. Must be less or equal to 999999999
	Upper *int `pulumi:"upper"`
}

// OptionsNextIdInput is an input type that accepts OptionsNextIdArgs and OptionsNextIdOutput values.
// You can construct a concrete instance of `OptionsNextIdInput` via:
//
//	OptionsNextIdArgs{...}
type OptionsNextIdInput interface {
	pulumi.Input

	ToOptionsNextIdOutput() OptionsNextIdOutput
	ToOptionsNextIdOutputWithContext(context.Context) OptionsNextIdOutput
}

type OptionsNextIdArgs struct {
	// The minimum number for the next free VM ID. Must be higher or equal to 100
	Lower pulumi.IntPtrInput `pulumi:"lower"`
	// The maximum number for the next free VM ID. Must be less or equal to 999999999
	Upper pulumi.IntPtrInput `pulumi:"upper"`
}

func (OptionsNextIdArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*OptionsNextId)(nil)).Elem()
}

func (i OptionsNextIdArgs) ToOptionsNextIdOutput() OptionsNextIdOutput {
	return i.ToOptionsNextIdOutputWithContext(context.Background())
}

func (i OptionsNextIdArgs) ToOptionsNextIdOutputWithContext(ctx context.Context) OptionsNextIdOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OptionsNextIdOutput)
}

func (i OptionsNextIdArgs) ToOptionsNextIdPtrOutput() OptionsNextIdPtrOutput {
	return i.ToOptionsNextIdPtrOutputWithContext(context.Background())
}

func (i OptionsNextIdArgs) ToOptionsNextIdPtrOutputWithContext(ctx context.Context) OptionsNextIdPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OptionsNextIdOutput).ToOptionsNextIdPtrOutputWithContext(ctx)
}

// OptionsNextIdPtrInput is an input type that accepts OptionsNextIdArgs, OptionsNextIdPtr and OptionsNextIdPtrOutput values.
// You can construct a concrete instance of `OptionsNextIdPtrInput` via:
//
//	        OptionsNextIdArgs{...}
//
//	or:
//
//	        nil
type OptionsNextIdPtrInput interface {
	pulumi.Input

	ToOptionsNextIdPtrOutput() OptionsNextIdPtrOutput
	ToOptionsNextIdPtrOutputWithContext(context.Context) OptionsNextIdPtrOutput
}

type optionsNextIdPtrType OptionsNextIdArgs

func OptionsNextIdPtr(v *OptionsNextIdArgs) OptionsNextIdPtrInput {
	return (*optionsNextIdPtrType)(v)
}

func (*optionsNextIdPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**OptionsNextId)(nil)).Elem()
}

func (i *optionsNextIdPtrType) ToOptionsNextIdPtrOutput() OptionsNextIdPtrOutput {
	return i.ToOptionsNextIdPtrOutputWithContext(context.Background())
}

func (i *optionsNextIdPtrType) ToOptionsNextIdPtrOutputWithContext(ctx context.Context) OptionsNextIdPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OptionsNextIdPtrOutput)
}

type OptionsNextIdOutput struct{ *pulumi.OutputState }

func (OptionsNextIdOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*OptionsNextId)(nil)).Elem()
}

func (o OptionsNextIdOutput) ToOptionsNextIdOutput() OptionsNextIdOutput {
	return o
}

func (o OptionsNextIdOutput) ToOptionsNextIdOutputWithContext(ctx context.Context) OptionsNextIdOutput {
	return o
}

func (o OptionsNextIdOutput) ToOptionsNextIdPtrOutput() OptionsNextIdPtrOutput {
	return o.ToOptionsNextIdPtrOutputWithContext(context.Background())
}

func (o OptionsNextIdOutput) ToOptionsNextIdPtrOutputWithContext(ctx context.Context) OptionsNextIdPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v OptionsNextId) *OptionsNextId {
		return &v
	}).(OptionsNextIdPtrOutput)
}

// The minimum number for the next free VM ID. Must be higher or equal to 100
func (o OptionsNextIdOutput) Lower() pulumi.IntPtrOutput {
	return o.ApplyT(func(v OptionsNextId) *int { return v.Lower }).(pulumi.IntPtrOutput)
}

// The maximum number for the next free VM ID. Must be less or equal to 999999999
func (o OptionsNextIdOutput) Upper() pulumi.IntPtrOutput {
	return o.ApplyT(func(v OptionsNextId) *int { return v.Upper }).(pulumi.IntPtrOutput)
}

type OptionsNextIdPtrOutput struct{ *pulumi.OutputState }

func (OptionsNextIdPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OptionsNextId)(nil)).Elem()
}

func (o OptionsNextIdPtrOutput) ToOptionsNextIdPtrOutput() OptionsNextIdPtrOutput {
	return o
}

func (o OptionsNextIdPtrOutput) ToOptionsNextIdPtrOutputWithContext(ctx context.Context) OptionsNextIdPtrOutput {
	return o
}

func (o OptionsNextIdPtrOutput) Elem() OptionsNextIdOutput {
	return o.ApplyT(func(v *OptionsNextId) OptionsNextId {
		if v != nil {
			return *v
		}
		var ret OptionsNextId
		return ret
	}).(OptionsNextIdOutput)
}

// The minimum number for the next free VM ID. Must be higher or equal to 100
func (o OptionsNextIdPtrOutput) Lower() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *OptionsNextId) *int {
		if v == nil {
			return nil
		}
		return v.Lower
	}).(pulumi.IntPtrOutput)
}

// The maximum number for the next free VM ID. Must be less or equal to 999999999
func (o OptionsNextIdPtrOutput) Upper() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *OptionsNextId) *int {
		if v == nil {
			return nil
		}
		return v.Upper
	}).(pulumi.IntPtrOutput)
}

type OptionsNotify struct {
	// Cluster-wide notification settings for the HA fencing mode. Must be `always` | `never`.
	HaFencingMode *string `pulumi:"haFencingMode"`
	// Cluster-wide notification settings for the HA fencing target.
	HaFencingTarget *string `pulumi:"haFencingTarget"`
	// Cluster-wide notification settings for package updates. Must be `auto` | `always` | `never`.
	PackageUpdates *string `pulumi:"packageUpdates"`
	// Cluster-wide notification settings for the package updates target.
	PackageUpdatesTarget *string `pulumi:"packageUpdatesTarget"`
	// Cluster-wide notification settings for replication. Must be `always` | `never`.
	Replication *string `pulumi:"replication"`
	// Cluster-wide notification settings for the replication target.
	ReplicationTarget *string `pulumi:"replicationTarget"`
}

// OptionsNotifyInput is an input type that accepts OptionsNotifyArgs and OptionsNotifyOutput values.
// You can construct a concrete instance of `OptionsNotifyInput` via:
//
//	OptionsNotifyArgs{...}
type OptionsNotifyInput interface {
	pulumi.Input

	ToOptionsNotifyOutput() OptionsNotifyOutput
	ToOptionsNotifyOutputWithContext(context.Context) OptionsNotifyOutput
}

type OptionsNotifyArgs struct {
	// Cluster-wide notification settings for the HA fencing mode. Must be `always` | `never`.
	HaFencingMode pulumi.StringPtrInput `pulumi:"haFencingMode"`
	// Cluster-wide notification settings for the HA fencing target.
	HaFencingTarget pulumi.StringPtrInput `pulumi:"haFencingTarget"`
	// Cluster-wide notification settings for package updates. Must be `auto` | `always` | `never`.
	PackageUpdates pulumi.StringPtrInput `pulumi:"packageUpdates"`
	// Cluster-wide notification settings for the package updates target.
	PackageUpdatesTarget pulumi.StringPtrInput `pulumi:"packageUpdatesTarget"`
	// Cluster-wide notification settings for replication. Must be `always` | `never`.
	Replication pulumi.StringPtrInput `pulumi:"replication"`
	// Cluster-wide notification settings for the replication target.
	ReplicationTarget pulumi.StringPtrInput `pulumi:"replicationTarget"`
}

func (OptionsNotifyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*OptionsNotify)(nil)).Elem()
}

func (i OptionsNotifyArgs) ToOptionsNotifyOutput() OptionsNotifyOutput {
	return i.ToOptionsNotifyOutputWithContext(context.Background())
}

func (i OptionsNotifyArgs) ToOptionsNotifyOutputWithContext(ctx context.Context) OptionsNotifyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OptionsNotifyOutput)
}

func (i OptionsNotifyArgs) ToOptionsNotifyPtrOutput() OptionsNotifyPtrOutput {
	return i.ToOptionsNotifyPtrOutputWithContext(context.Background())
}

func (i OptionsNotifyArgs) ToOptionsNotifyPtrOutputWithContext(ctx context.Context) OptionsNotifyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OptionsNotifyOutput).ToOptionsNotifyPtrOutputWithContext(ctx)
}

// OptionsNotifyPtrInput is an input type that accepts OptionsNotifyArgs, OptionsNotifyPtr and OptionsNotifyPtrOutput values.
// You can construct a concrete instance of `OptionsNotifyPtrInput` via:
//
//	        OptionsNotifyArgs{...}
//
//	or:
//
//	        nil
type OptionsNotifyPtrInput interface {
	pulumi.Input

	ToOptionsNotifyPtrOutput() OptionsNotifyPtrOutput
	ToOptionsNotifyPtrOutputWithContext(context.Context) OptionsNotifyPtrOutput
}

type optionsNotifyPtrType OptionsNotifyArgs

func OptionsNotifyPtr(v *OptionsNotifyArgs) OptionsNotifyPtrInput {
	return (*optionsNotifyPtrType)(v)
}

func (*optionsNotifyPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**OptionsNotify)(nil)).Elem()
}

func (i *optionsNotifyPtrType) ToOptionsNotifyPtrOutput() OptionsNotifyPtrOutput {
	return i.ToOptionsNotifyPtrOutputWithContext(context.Background())
}

func (i *optionsNotifyPtrType) ToOptionsNotifyPtrOutputWithContext(ctx context.Context) OptionsNotifyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OptionsNotifyPtrOutput)
}

type OptionsNotifyOutput struct{ *pulumi.OutputState }

func (OptionsNotifyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*OptionsNotify)(nil)).Elem()
}

func (o OptionsNotifyOutput) ToOptionsNotifyOutput() OptionsNotifyOutput {
	return o
}

func (o OptionsNotifyOutput) ToOptionsNotifyOutputWithContext(ctx context.Context) OptionsNotifyOutput {
	return o
}

func (o OptionsNotifyOutput) ToOptionsNotifyPtrOutput() OptionsNotifyPtrOutput {
	return o.ToOptionsNotifyPtrOutputWithContext(context.Background())
}

func (o OptionsNotifyOutput) ToOptionsNotifyPtrOutputWithContext(ctx context.Context) OptionsNotifyPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v OptionsNotify) *OptionsNotify {
		return &v
	}).(OptionsNotifyPtrOutput)
}

// Cluster-wide notification settings for the HA fencing mode. Must be `always` | `never`.
func (o OptionsNotifyOutput) HaFencingMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v OptionsNotify) *string { return v.HaFencingMode }).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for the HA fencing target.
func (o OptionsNotifyOutput) HaFencingTarget() pulumi.StringPtrOutput {
	return o.ApplyT(func(v OptionsNotify) *string { return v.HaFencingTarget }).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for package updates. Must be `auto` | `always` | `never`.
func (o OptionsNotifyOutput) PackageUpdates() pulumi.StringPtrOutput {
	return o.ApplyT(func(v OptionsNotify) *string { return v.PackageUpdates }).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for the package updates target.
func (o OptionsNotifyOutput) PackageUpdatesTarget() pulumi.StringPtrOutput {
	return o.ApplyT(func(v OptionsNotify) *string { return v.PackageUpdatesTarget }).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for replication. Must be `always` | `never`.
func (o OptionsNotifyOutput) Replication() pulumi.StringPtrOutput {
	return o.ApplyT(func(v OptionsNotify) *string { return v.Replication }).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for the replication target.
func (o OptionsNotifyOutput) ReplicationTarget() pulumi.StringPtrOutput {
	return o.ApplyT(func(v OptionsNotify) *string { return v.ReplicationTarget }).(pulumi.StringPtrOutput)
}

type OptionsNotifyPtrOutput struct{ *pulumi.OutputState }

func (OptionsNotifyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OptionsNotify)(nil)).Elem()
}

func (o OptionsNotifyPtrOutput) ToOptionsNotifyPtrOutput() OptionsNotifyPtrOutput {
	return o
}

func (o OptionsNotifyPtrOutput) ToOptionsNotifyPtrOutputWithContext(ctx context.Context) OptionsNotifyPtrOutput {
	return o
}

func (o OptionsNotifyPtrOutput) Elem() OptionsNotifyOutput {
	return o.ApplyT(func(v *OptionsNotify) OptionsNotify {
		if v != nil {
			return *v
		}
		var ret OptionsNotify
		return ret
	}).(OptionsNotifyOutput)
}

// Cluster-wide notification settings for the HA fencing mode. Must be `always` | `never`.
func (o OptionsNotifyPtrOutput) HaFencingMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OptionsNotify) *string {
		if v == nil {
			return nil
		}
		return v.HaFencingMode
	}).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for the HA fencing target.
func (o OptionsNotifyPtrOutput) HaFencingTarget() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OptionsNotify) *string {
		if v == nil {
			return nil
		}
		return v.HaFencingTarget
	}).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for package updates. Must be `auto` | `always` | `never`.
func (o OptionsNotifyPtrOutput) PackageUpdates() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OptionsNotify) *string {
		if v == nil {
			return nil
		}
		return v.PackageUpdates
	}).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for the package updates target.
func (o OptionsNotifyPtrOutput) PackageUpdatesTarget() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OptionsNotify) *string {
		if v == nil {
			return nil
		}
		return v.PackageUpdatesTarget
	}).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for replication. Must be `always` | `never`.
func (o OptionsNotifyPtrOutput) Replication() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OptionsNotify) *string {
		if v == nil {
			return nil
		}
		return v.Replication
	}).(pulumi.StringPtrOutput)
}

// Cluster-wide notification settings for the replication target.
func (o OptionsNotifyPtrOutput) ReplicationTarget() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OptionsNotify) *string {
		if v == nil {
			return nil
		}
		return v.ReplicationTarget
	}).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OptionsNextIdInput)(nil)).Elem(), OptionsNextIdArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*OptionsNextIdPtrInput)(nil)).Elem(), OptionsNextIdArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*OptionsNotifyInput)(nil)).Elem(), OptionsNotifyArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*OptionsNotifyPtrInput)(nil)).Elem(), OptionsNotifyArgs{})
	pulumi.RegisterOutputType(OptionsNextIdOutput{})
	pulumi.RegisterOutputType(OptionsNextIdPtrOutput{})
	pulumi.RegisterOutputType(OptionsNotifyOutput{})
	pulumi.RegisterOutputType(OptionsNotifyPtrOutput{})
}