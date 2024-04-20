// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Retrieves a list of hardware mapping resources.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as proxmoxve from "@pulumi/proxmoxve";
 *
 * const example-pci = proxmoxve.Hardware.getMappings({
 *     checkNode: "pve",
 *     type: "pci",
 * });
 * const example-usb = proxmoxve.Hardware.getMappings({
 *     checkNode: "pve",
 *     type: "usb",
 * });
 * export const dataProxmoxVirtualEnvironmentHardwareMappingsPci = example_pci;
 * export const dataProxmoxVirtualEnvironmentHardwareMappingsUsb = example_usb;
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getMappings(args: GetMappingsArgs, opts?: pulumi.InvokeOptions): Promise<GetMappingsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("proxmoxve:Hardware/getMappings:getMappings", {
        "checkNode": args.checkNode,
        "type": args.type,
    }, opts);
}

/**
 * A collection of arguments for invoking getMappings.
 */
export interface GetMappingsArgs {
    /**
     * The name of the node whose configurations should be checked for correctness.
     */
    checkNode?: string;
    /**
     * The type of the hardware mappings.
     */
    type: string;
}

/**
 * A collection of values returned by getMappings.
 */
export interface GetMappingsResult {
    /**
     * The name of the node whose configurations should be checked for correctness.
     */
    readonly checkNode?: string;
    /**
     * Might contain relevant diagnostics about incorrect configurations.
     */
    readonly checks: outputs.Hardware.GetMappingsCheck[];
    /**
     * The unique identifier of this hardware mappings data source.
     */
    readonly id: string;
    /**
     * The identifiers of the hardware mappings.
     */
    readonly ids: string[];
    /**
     * The type of the hardware mappings.
     */
    readonly type: string;
}
/**
 * Retrieves a list of hardware mapping resources.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as proxmoxve from "@pulumi/proxmoxve";
 *
 * const example-pci = proxmoxve.Hardware.getMappings({
 *     checkNode: "pve",
 *     type: "pci",
 * });
 * const example-usb = proxmoxve.Hardware.getMappings({
 *     checkNode: "pve",
 *     type: "usb",
 * });
 * export const dataProxmoxVirtualEnvironmentHardwareMappingsPci = example_pci;
 * export const dataProxmoxVirtualEnvironmentHardwareMappingsUsb = example_usb;
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getMappingsOutput(args: GetMappingsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetMappingsResult> {
    return pulumi.output(args).apply((a: any) => getMappings(a, opts))
}

/**
 * A collection of arguments for invoking getMappings.
 */
export interface GetMappingsOutputArgs {
    /**
     * The name of the node whose configurations should be checked for correctness.
     */
    checkNode?: pulumi.Input<string>;
    /**
     * The type of the hardware mappings.
     */
    type: pulumi.Input<string>;
}
