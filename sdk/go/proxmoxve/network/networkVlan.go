// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"context"
	"reflect"

	"errors"
	"github.com/muhlba91/pulumi-proxmoxve/sdk/v5/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a Linux VLAN network interface in a Proxmox VE node.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/muhlba91/pulumi-proxmoxve/sdk/v5/go/proxmoxve/Network"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			// using VLAN tag
//			_, err := Network.NewNetworkVlan(ctx, "vlan99", &Network.NetworkVlanArgs{
//				Comment:  pulumi.String("VLAN 99"),
//				NodeName: pulumi.String("pve"),
//			})
//			if err != nil {
//				return err
//			}
//			// using custom network interface name
//			_, err = Network.NewNetworkVlan(ctx, "vlan98", &Network.NetworkVlanArgs{
//				Comment:   pulumi.String("VLAN 98"),
//				Interface: pulumi.String("eno0"),
//				NodeName:  pulumi.String("pve"),
//				Vlan:      pulumi.Int(98),
//			})
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
//	#Interfaces can be imported using the `node_name:iface` format, e.g.
//
// ```sh
// $ pulumi import proxmoxve:Network/networkVlan:NetworkVlan vlan99 pve:vlan99
// ```
type NetworkVlan struct {
	pulumi.CustomResourceState

	// The interface IPv4/CIDR address.
	Address pulumi.StringPtrOutput `pulumi:"address"`
	// The interface IPv6/CIDR address.
	Address6 pulumi.StringPtrOutput `pulumi:"address6"`
	// Automatically start interface on boot (defaults to `true`).
	Autostart pulumi.BoolOutput `pulumi:"autostart"`
	// Comment for the interface.
	Comment pulumi.StringPtrOutput `pulumi:"comment"`
	// Default gateway address.
	Gateway pulumi.StringPtrOutput `pulumi:"gateway"`
	// Default IPv6 gateway address.
	Gateway6 pulumi.StringPtrOutput `pulumi:"gateway6"`
	// The VLAN raw device. See also `name`.
	Interface pulumi.StringOutput `pulumi:"interface"`
	// The interface MTU.
	Mtu pulumi.IntPtrOutput `pulumi:"mtu"`
	// The interface name. Either add the VLAN tag number to an existing interface name, e.g. `ens18.21` (and do not set `interface` and `vlan`), or use custom name, e.g. `vlanLab` (`interface` and `vlan` are then required).
	Name pulumi.StringOutput `pulumi:"name"`
	// The name of the node.
	NodeName pulumi.StringOutput `pulumi:"nodeName"`
	// The VLAN tag. See also `name`.
	Vlan pulumi.IntOutput `pulumi:"vlan"`
}

// NewNetworkVlan registers a new resource with the given unique name, arguments, and options.
func NewNetworkVlan(ctx *pulumi.Context,
	name string, args *NetworkVlanArgs, opts ...pulumi.ResourceOption) (*NetworkVlan, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.NodeName == nil {
		return nil, errors.New("invalid value for required argument 'NodeName'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource NetworkVlan
	err := ctx.RegisterResource("proxmoxve:Network/networkVlan:NetworkVlan", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkVlan gets an existing NetworkVlan resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkVlan(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkVlanState, opts ...pulumi.ResourceOption) (*NetworkVlan, error) {
	var resource NetworkVlan
	err := ctx.ReadResource("proxmoxve:Network/networkVlan:NetworkVlan", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkVlan resources.
type networkVlanState struct {
	// The interface IPv4/CIDR address.
	Address *string `pulumi:"address"`
	// The interface IPv6/CIDR address.
	Address6 *string `pulumi:"address6"`
	// Automatically start interface on boot (defaults to `true`).
	Autostart *bool `pulumi:"autostart"`
	// Comment for the interface.
	Comment *string `pulumi:"comment"`
	// Default gateway address.
	Gateway *string `pulumi:"gateway"`
	// Default IPv6 gateway address.
	Gateway6 *string `pulumi:"gateway6"`
	// The VLAN raw device. See also `name`.
	Interface *string `pulumi:"interface"`
	// The interface MTU.
	Mtu *int `pulumi:"mtu"`
	// The interface name. Either add the VLAN tag number to an existing interface name, e.g. `ens18.21` (and do not set `interface` and `vlan`), or use custom name, e.g. `vlanLab` (`interface` and `vlan` are then required).
	Name *string `pulumi:"name"`
	// The name of the node.
	NodeName *string `pulumi:"nodeName"`
	// The VLAN tag. See also `name`.
	Vlan *int `pulumi:"vlan"`
}

type NetworkVlanState struct {
	// The interface IPv4/CIDR address.
	Address pulumi.StringPtrInput
	// The interface IPv6/CIDR address.
	Address6 pulumi.StringPtrInput
	// Automatically start interface on boot (defaults to `true`).
	Autostart pulumi.BoolPtrInput
	// Comment for the interface.
	Comment pulumi.StringPtrInput
	// Default gateway address.
	Gateway pulumi.StringPtrInput
	// Default IPv6 gateway address.
	Gateway6 pulumi.StringPtrInput
	// The VLAN raw device. See also `name`.
	Interface pulumi.StringPtrInput
	// The interface MTU.
	Mtu pulumi.IntPtrInput
	// The interface name. Either add the VLAN tag number to an existing interface name, e.g. `ens18.21` (and do not set `interface` and `vlan`), or use custom name, e.g. `vlanLab` (`interface` and `vlan` are then required).
	Name pulumi.StringPtrInput
	// The name of the node.
	NodeName pulumi.StringPtrInput
	// The VLAN tag. See also `name`.
	Vlan pulumi.IntPtrInput
}

func (NetworkVlanState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkVlanState)(nil)).Elem()
}

type networkVlanArgs struct {
	// The interface IPv4/CIDR address.
	Address *string `pulumi:"address"`
	// The interface IPv6/CIDR address.
	Address6 *string `pulumi:"address6"`
	// Automatically start interface on boot (defaults to `true`).
	Autostart *bool `pulumi:"autostart"`
	// Comment for the interface.
	Comment *string `pulumi:"comment"`
	// Default gateway address.
	Gateway *string `pulumi:"gateway"`
	// Default IPv6 gateway address.
	Gateway6 *string `pulumi:"gateway6"`
	// The VLAN raw device. See also `name`.
	Interface *string `pulumi:"interface"`
	// The interface MTU.
	Mtu *int `pulumi:"mtu"`
	// The interface name. Either add the VLAN tag number to an existing interface name, e.g. `ens18.21` (and do not set `interface` and `vlan`), or use custom name, e.g. `vlanLab` (`interface` and `vlan` are then required).
	Name *string `pulumi:"name"`
	// The name of the node.
	NodeName string `pulumi:"nodeName"`
	// The VLAN tag. See also `name`.
	Vlan *int `pulumi:"vlan"`
}

// The set of arguments for constructing a NetworkVlan resource.
type NetworkVlanArgs struct {
	// The interface IPv4/CIDR address.
	Address pulumi.StringPtrInput
	// The interface IPv6/CIDR address.
	Address6 pulumi.StringPtrInput
	// Automatically start interface on boot (defaults to `true`).
	Autostart pulumi.BoolPtrInput
	// Comment for the interface.
	Comment pulumi.StringPtrInput
	// Default gateway address.
	Gateway pulumi.StringPtrInput
	// Default IPv6 gateway address.
	Gateway6 pulumi.StringPtrInput
	// The VLAN raw device. See also `name`.
	Interface pulumi.StringPtrInput
	// The interface MTU.
	Mtu pulumi.IntPtrInput
	// The interface name. Either add the VLAN tag number to an existing interface name, e.g. `ens18.21` (and do not set `interface` and `vlan`), or use custom name, e.g. `vlanLab` (`interface` and `vlan` are then required).
	Name pulumi.StringPtrInput
	// The name of the node.
	NodeName pulumi.StringInput
	// The VLAN tag. See also `name`.
	Vlan pulumi.IntPtrInput
}

func (NetworkVlanArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkVlanArgs)(nil)).Elem()
}

type NetworkVlanInput interface {
	pulumi.Input

	ToNetworkVlanOutput() NetworkVlanOutput
	ToNetworkVlanOutputWithContext(ctx context.Context) NetworkVlanOutput
}

func (*NetworkVlan) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkVlan)(nil)).Elem()
}

func (i *NetworkVlan) ToNetworkVlanOutput() NetworkVlanOutput {
	return i.ToNetworkVlanOutputWithContext(context.Background())
}

func (i *NetworkVlan) ToNetworkVlanOutputWithContext(ctx context.Context) NetworkVlanOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkVlanOutput)
}

// NetworkVlanArrayInput is an input type that accepts NetworkVlanArray and NetworkVlanArrayOutput values.
// You can construct a concrete instance of `NetworkVlanArrayInput` via:
//
//	NetworkVlanArray{ NetworkVlanArgs{...} }
type NetworkVlanArrayInput interface {
	pulumi.Input

	ToNetworkVlanArrayOutput() NetworkVlanArrayOutput
	ToNetworkVlanArrayOutputWithContext(context.Context) NetworkVlanArrayOutput
}

type NetworkVlanArray []NetworkVlanInput

func (NetworkVlanArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkVlan)(nil)).Elem()
}

func (i NetworkVlanArray) ToNetworkVlanArrayOutput() NetworkVlanArrayOutput {
	return i.ToNetworkVlanArrayOutputWithContext(context.Background())
}

func (i NetworkVlanArray) ToNetworkVlanArrayOutputWithContext(ctx context.Context) NetworkVlanArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkVlanArrayOutput)
}

// NetworkVlanMapInput is an input type that accepts NetworkVlanMap and NetworkVlanMapOutput values.
// You can construct a concrete instance of `NetworkVlanMapInput` via:
//
//	NetworkVlanMap{ "key": NetworkVlanArgs{...} }
type NetworkVlanMapInput interface {
	pulumi.Input

	ToNetworkVlanMapOutput() NetworkVlanMapOutput
	ToNetworkVlanMapOutputWithContext(context.Context) NetworkVlanMapOutput
}

type NetworkVlanMap map[string]NetworkVlanInput

func (NetworkVlanMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkVlan)(nil)).Elem()
}

func (i NetworkVlanMap) ToNetworkVlanMapOutput() NetworkVlanMapOutput {
	return i.ToNetworkVlanMapOutputWithContext(context.Background())
}

func (i NetworkVlanMap) ToNetworkVlanMapOutputWithContext(ctx context.Context) NetworkVlanMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkVlanMapOutput)
}

type NetworkVlanOutput struct{ *pulumi.OutputState }

func (NetworkVlanOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkVlan)(nil)).Elem()
}

func (o NetworkVlanOutput) ToNetworkVlanOutput() NetworkVlanOutput {
	return o
}

func (o NetworkVlanOutput) ToNetworkVlanOutputWithContext(ctx context.Context) NetworkVlanOutput {
	return o
}

// The interface IPv4/CIDR address.
func (o NetworkVlanOutput) Address() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.StringPtrOutput { return v.Address }).(pulumi.StringPtrOutput)
}

// The interface IPv6/CIDR address.
func (o NetworkVlanOutput) Address6() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.StringPtrOutput { return v.Address6 }).(pulumi.StringPtrOutput)
}

// Automatically start interface on boot (defaults to `true`).
func (o NetworkVlanOutput) Autostart() pulumi.BoolOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.BoolOutput { return v.Autostart }).(pulumi.BoolOutput)
}

// Comment for the interface.
func (o NetworkVlanOutput) Comment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.StringPtrOutput { return v.Comment }).(pulumi.StringPtrOutput)
}

// Default gateway address.
func (o NetworkVlanOutput) Gateway() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.StringPtrOutput { return v.Gateway }).(pulumi.StringPtrOutput)
}

// Default IPv6 gateway address.
func (o NetworkVlanOutput) Gateway6() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.StringPtrOutput { return v.Gateway6 }).(pulumi.StringPtrOutput)
}

// The VLAN raw device. See also `name`.
func (o NetworkVlanOutput) Interface() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.StringOutput { return v.Interface }).(pulumi.StringOutput)
}

// The interface MTU.
func (o NetworkVlanOutput) Mtu() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.IntPtrOutput { return v.Mtu }).(pulumi.IntPtrOutput)
}

// The interface name. Either add the VLAN tag number to an existing interface name, e.g. `ens18.21` (and do not set `interface` and `vlan`), or use custom name, e.g. `vlanLab` (`interface` and `vlan` are then required).
func (o NetworkVlanOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The name of the node.
func (o NetworkVlanOutput) NodeName() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.StringOutput { return v.NodeName }).(pulumi.StringOutput)
}

// The VLAN tag. See also `name`.
func (o NetworkVlanOutput) Vlan() pulumi.IntOutput {
	return o.ApplyT(func(v *NetworkVlan) pulumi.IntOutput { return v.Vlan }).(pulumi.IntOutput)
}

type NetworkVlanArrayOutput struct{ *pulumi.OutputState }

func (NetworkVlanArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*NetworkVlan)(nil)).Elem()
}

func (o NetworkVlanArrayOutput) ToNetworkVlanArrayOutput() NetworkVlanArrayOutput {
	return o
}

func (o NetworkVlanArrayOutput) ToNetworkVlanArrayOutputWithContext(ctx context.Context) NetworkVlanArrayOutput {
	return o
}

func (o NetworkVlanArrayOutput) Index(i pulumi.IntInput) NetworkVlanOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *NetworkVlan {
		return vs[0].([]*NetworkVlan)[vs[1].(int)]
	}).(NetworkVlanOutput)
}

type NetworkVlanMapOutput struct{ *pulumi.OutputState }

func (NetworkVlanMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*NetworkVlan)(nil)).Elem()
}

func (o NetworkVlanMapOutput) ToNetworkVlanMapOutput() NetworkVlanMapOutput {
	return o
}

func (o NetworkVlanMapOutput) ToNetworkVlanMapOutputWithContext(ctx context.Context) NetworkVlanMapOutput {
	return o
}

func (o NetworkVlanMapOutput) MapIndex(k pulumi.StringInput) NetworkVlanOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *NetworkVlan {
		return vs[0].(map[string]*NetworkVlan)[vs[1].(string)]
	}).(NetworkVlanOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkVlanInput)(nil)).Elem(), &NetworkVlan{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkVlanArrayInput)(nil)).Elem(), NetworkVlanArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkVlanMapInput)(nil)).Elem(), NetworkVlanMap{})
	pulumi.RegisterOutputType(NetworkVlanOutput{})
	pulumi.RegisterOutputType(NetworkVlanArrayOutput{})
	pulumi.RegisterOutputType(NetworkVlanMapOutput{})
}
