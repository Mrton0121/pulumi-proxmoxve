// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The provider type for the proxmox package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'proxmoxve';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === "pulumi:providers:" + Provider.__pulumiType;
    }

    /**
     * The API token for the Proxmox VE API.
     */
    public readonly apiToken!: pulumi.Output<string | undefined>;
    /**
     * The pre-authenticated Ticket for the Proxmox VE API.
     */
    public readonly authTicket!: pulumi.Output<string | undefined>;
    /**
     * The pre-authenticated CSRF Prevention Token for the Proxmox VE API.
     */
    public readonly csrfPreventionToken!: pulumi.Output<string | undefined>;
    /**
     * The endpoint for the Proxmox VE API.
     */
    public readonly endpoint!: pulumi.Output<string | undefined>;
    /**
     * The minimum required TLS version for API calls.Supported values: `1.0|1.1|1.2|1.3`. Defaults to `1.3`.
     */
    public readonly minTls!: pulumi.Output<string | undefined>;
    /**
     * The one-time password for the Proxmox VE API.
     *
     * @deprecated The `otp` attribute is deprecated and will be removed in a future release. Please use the `apiToken` attribute instead.
     */
    public readonly otp!: pulumi.Output<string | undefined>;
    /**
     * The password for the Proxmox VE API.
     */
    public readonly password!: pulumi.Output<string | undefined>;
    /**
     * The alternative temporary directory.
     */
    public readonly tmpDir!: pulumi.Output<string | undefined>;
    /**
     * The username for the Proxmox VE API.
     */
    public readonly username!: pulumi.Output<string | undefined>;

    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        {
            resourceInputs["apiToken"] = args?.apiToken ? pulumi.secret(args.apiToken) : undefined;
            resourceInputs["authTicket"] = args?.authTicket ? pulumi.secret(args.authTicket) : undefined;
            resourceInputs["csrfPreventionToken"] = args?.csrfPreventionToken ? pulumi.secret(args.csrfPreventionToken) : undefined;
            resourceInputs["endpoint"] = args ? args.endpoint : undefined;
            resourceInputs["insecure"] = pulumi.output(args ? args.insecure : undefined).apply(JSON.stringify);
            resourceInputs["minTls"] = args ? args.minTls : undefined;
            resourceInputs["otp"] = args ? args.otp : undefined;
            resourceInputs["password"] = args?.password ? pulumi.secret(args.password) : undefined;
            resourceInputs["randomVmIdEnd"] = pulumi.output(args ? args.randomVmIdEnd : undefined).apply(JSON.stringify);
            resourceInputs["randomVmIdStart"] = pulumi.output(args ? args.randomVmIdStart : undefined).apply(JSON.stringify);
            resourceInputs["randomVmIds"] = pulumi.output(args ? args.randomVmIds : undefined).apply(JSON.stringify);
            resourceInputs["ssh"] = pulumi.output(args ? args.ssh : undefined).apply(JSON.stringify);
            resourceInputs["tmpDir"] = args ? args.tmpDir : undefined;
            resourceInputs["username"] = args ? args.username : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["apiToken", "authTicket", "csrfPreventionToken", "password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Provider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    /**
     * The API token for the Proxmox VE API.
     */
    apiToken?: pulumi.Input<string>;
    /**
     * The pre-authenticated Ticket for the Proxmox VE API.
     */
    authTicket?: pulumi.Input<string>;
    /**
     * The pre-authenticated CSRF Prevention Token for the Proxmox VE API.
     */
    csrfPreventionToken?: pulumi.Input<string>;
    /**
     * The endpoint for the Proxmox VE API.
     */
    endpoint?: pulumi.Input<string>;
    /**
     * Whether to skip the TLS verification step.
     */
    insecure?: pulumi.Input<boolean>;
    /**
     * The minimum required TLS version for API calls.Supported values: `1.0|1.1|1.2|1.3`. Defaults to `1.3`.
     */
    minTls?: pulumi.Input<string>;
    /**
     * The one-time password for the Proxmox VE API.
     *
     * @deprecated The `otp` attribute is deprecated and will be removed in a future release. Please use the `apiToken` attribute instead.
     */
    otp?: pulumi.Input<string>;
    /**
     * The password for the Proxmox VE API.
     */
    password?: pulumi.Input<string>;
    /**
     * The ending number for random VM / Container IDs.
     */
    randomVmIdEnd?: pulumi.Input<number>;
    /**
     * The starting number for random VM / Container IDs.
     */
    randomVmIdStart?: pulumi.Input<number>;
    /**
     * Whether to generate random VM / Container IDs.
     */
    randomVmIds?: pulumi.Input<boolean>;
    /**
     * The SSH configuration for the Proxmox nodes.
     */
    ssh?: pulumi.Input<inputs.ProviderSsh>;
    /**
     * The alternative temporary directory.
     */
    tmpDir?: pulumi.Input<string>;
    /**
     * The username for the Proxmox VE API.
     */
    username?: pulumi.Input<string>;
}
