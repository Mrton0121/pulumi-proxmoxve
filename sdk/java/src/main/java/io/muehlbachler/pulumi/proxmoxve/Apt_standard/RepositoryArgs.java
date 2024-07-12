// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.Apt_standard;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class RepositoryArgs extends com.pulumi.resources.ResourceArgs {

    public static final RepositoryArgs Empty = new RepositoryArgs();

    /**
     * The handle of the APT standard repository. Must be `ceph-quincy-enterprise` | `ceph-quincy-no-subscription` | `ceph-quincy-test` | `ceph-reef-enterprise` | `ceph-reef-no-subscription` | `ceph-reef-test` | `enterprise` | `no-subscription` | `test`.
     * 
     */
    @Import(name="handle", required=true)
    private Output<String> handle;

    /**
     * @return The handle of the APT standard repository. Must be `ceph-quincy-enterprise` | `ceph-quincy-no-subscription` | `ceph-quincy-test` | `ceph-reef-enterprise` | `ceph-reef-no-subscription` | `ceph-reef-test` | `enterprise` | `no-subscription` | `test`.
     * 
     */
    public Output<String> handle() {
        return this.handle;
    }

    /**
     * The name of the target Proxmox VE node.
     * 
     */
    @Import(name="node", required=true)
    private Output<String> node;

    /**
     * @return The name of the target Proxmox VE node.
     * 
     */
    public Output<String> node() {
        return this.node;
    }

    private RepositoryArgs() {}

    private RepositoryArgs(RepositoryArgs $) {
        this.handle = $.handle;
        this.node = $.node;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(RepositoryArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private RepositoryArgs $;

        public Builder() {
            $ = new RepositoryArgs();
        }

        public Builder(RepositoryArgs defaults) {
            $ = new RepositoryArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param handle The handle of the APT standard repository. Must be `ceph-quincy-enterprise` | `ceph-quincy-no-subscription` | `ceph-quincy-test` | `ceph-reef-enterprise` | `ceph-reef-no-subscription` | `ceph-reef-test` | `enterprise` | `no-subscription` | `test`.
         * 
         * @return builder
         * 
         */
        public Builder handle(Output<String> handle) {
            $.handle = handle;
            return this;
        }

        /**
         * @param handle The handle of the APT standard repository. Must be `ceph-quincy-enterprise` | `ceph-quincy-no-subscription` | `ceph-quincy-test` | `ceph-reef-enterprise` | `ceph-reef-no-subscription` | `ceph-reef-test` | `enterprise` | `no-subscription` | `test`.
         * 
         * @return builder
         * 
         */
        public Builder handle(String handle) {
            return handle(Output.of(handle));
        }

        /**
         * @param node The name of the target Proxmox VE node.
         * 
         * @return builder
         * 
         */
        public Builder node(Output<String> node) {
            $.node = node;
            return this;
        }

        /**
         * @param node The name of the target Proxmox VE node.
         * 
         * @return builder
         * 
         */
        public Builder node(String node) {
            return node(Output.of(node));
        }

        public RepositoryArgs build() {
            if ($.handle == null) {
                throw new MissingRequiredPropertyException("RepositoryArgs", "handle");
            }
            if ($.node == null) {
                throw new MissingRequiredPropertyException("RepositoryArgs", "node");
            }
            return $;
        }
    }

}