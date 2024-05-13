// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import io.muehlbachler.pulumi.proxmoxve.AclArgs;
import io.muehlbachler.pulumi.proxmoxve.Utilities;
import io.muehlbachler.pulumi.proxmoxve.inputs.AclState;
import java.lang.Boolean;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Manages ACLs on the Proxmox cluster.
 * 
 * ACLs are used to control access to resources in the Proxmox cluster.
 * Each ACL consists of a path, a user, group or token, a role, and a flag to allow propagation of permissions.
 * 
 * ## Example Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.proxmoxve.Permission.User;
 * import com.pulumi.proxmoxve.Permission.UserArgs;
 * import com.pulumi.proxmoxve.Permission.Role;
 * import com.pulumi.proxmoxve.Permission.RoleArgs;
 * import com.pulumi.proxmoxve.Acl;
 * import com.pulumi.proxmoxve.AclArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var operationsAutomation = new User(&#34;operationsAutomation&#34;, UserArgs.builder()        
 *             .comment(&#34;Managed by Terraform&#34;)
 *             .password(&#34;a-strong-password&#34;)
 *             .userId(&#34;operations-automation@pve&#34;)
 *             .build());
 * 
 *         var operationsMonitoring = new Role(&#34;operationsMonitoring&#34;, RoleArgs.builder()        
 *             .roleId(&#34;operations-monitoring&#34;)
 *             .privileges(&#34;VM.Monitor&#34;)
 *             .build());
 * 
 *         var operationsAutomationMonitoring = new Acl(&#34;operationsAutomationMonitoring&#34;, AclArgs.builder()        
 *             .userId(operationsAutomation.userId())
 *             .roleId(operationsMonitoring.roleId())
 *             .path(&#34;/vms/1234&#34;)
 *             .propagate(true)
 *             .build());
 * 
 *     }
 * }
 * ```
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * #!/usr/bin/env sh
 * 
 * ACL can be imported using its unique identifier, e.g.: {path}?{group|user@realm|user@realm!token}?{role}
 * 
 * ```sh
 * $ pulumi import proxmoxve:index/acl:Acl operations_automation_monitoring /?monitor@pve?operations-monitoring
 * ```
 * 
 */
@ResourceType(type="proxmoxve:index/acl:Acl")
public class Acl extends com.pulumi.resources.CustomResource {
    /**
     * The group the ACL should apply to (mutually exclusive with `token_id` and `user_id`)
     * 
     */
    @Export(name="groupId", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> groupId;

    /**
     * @return The group the ACL should apply to (mutually exclusive with `token_id` and `user_id`)
     * 
     */
    public Output<Optional<String>> groupId() {
        return Codegen.optional(this.groupId);
    }
    /**
     * Access control path
     * 
     */
    @Export(name="path", refs={String.class}, tree="[0]")
    private Output<String> path;

    /**
     * @return Access control path
     * 
     */
    public Output<String> path() {
        return this.path;
    }
    /**
     * Allow to propagate (inherit) permissions.
     * 
     */
    @Export(name="propagate", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> propagate;

    /**
     * @return Allow to propagate (inherit) permissions.
     * 
     */
    public Output<Boolean> propagate() {
        return this.propagate;
    }
    /**
     * The role to apply
     * 
     */
    @Export(name="roleId", refs={String.class}, tree="[0]")
    private Output<String> roleId;

    /**
     * @return The role to apply
     * 
     */
    public Output<String> roleId() {
        return this.roleId;
    }
    /**
     * The token the ACL should apply to (mutually exclusive with `group_id` and `user_id`)
     * 
     */
    @Export(name="tokenId", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> tokenId;

    /**
     * @return The token the ACL should apply to (mutually exclusive with `group_id` and `user_id`)
     * 
     */
    public Output<Optional<String>> tokenId() {
        return Codegen.optional(this.tokenId);
    }
    /**
     * The user the ACL should apply to (mutually exclusive with `group_id` and `token_id`)
     * 
     */
    @Export(name="userId", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> userId;

    /**
     * @return The user the ACL should apply to (mutually exclusive with `group_id` and `token_id`)
     * 
     */
    public Output<Optional<String>> userId() {
        return Codegen.optional(this.userId);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Acl(String name) {
        this(name, AclArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Acl(String name, AclArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Acl(String name, AclArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("proxmoxve:index/acl:Acl", name, args == null ? AclArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Acl(String name, Output<String> id, @Nullable AclState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("proxmoxve:index/acl:Acl", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static Acl get(String name, Output<String> id, @Nullable AclState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Acl(name, id, state, options);
    }
}