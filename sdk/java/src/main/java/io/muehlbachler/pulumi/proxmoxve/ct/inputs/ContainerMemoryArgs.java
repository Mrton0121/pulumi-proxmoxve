// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.CT.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ContainerMemoryArgs extends com.pulumi.resources.ResourceArgs {

    public static final ContainerMemoryArgs Empty = new ContainerMemoryArgs();

    /**
     * The dedicated memory in megabytes (defaults
     * to `512`).
     * 
     */
    @Import(name="dedicated")
    private @Nullable Output<Integer> dedicated;

    /**
     * @return The dedicated memory in megabytes (defaults
     * to `512`).
     * 
     */
    public Optional<Output<Integer>> dedicated() {
        return Optional.ofNullable(this.dedicated);
    }

    /**
     * The swap size in megabytes (defaults to `0`).
     * 
     */
    @Import(name="swap")
    private @Nullable Output<Integer> swap;

    /**
     * @return The swap size in megabytes (defaults to `0`).
     * 
     */
    public Optional<Output<Integer>> swap() {
        return Optional.ofNullable(this.swap);
    }

    private ContainerMemoryArgs() {}

    private ContainerMemoryArgs(ContainerMemoryArgs $) {
        this.dedicated = $.dedicated;
        this.swap = $.swap;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ContainerMemoryArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ContainerMemoryArgs $;

        public Builder() {
            $ = new ContainerMemoryArgs();
        }

        public Builder(ContainerMemoryArgs defaults) {
            $ = new ContainerMemoryArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param dedicated The dedicated memory in megabytes (defaults
         * to `512`).
         * 
         * @return builder
         * 
         */
        public Builder dedicated(@Nullable Output<Integer> dedicated) {
            $.dedicated = dedicated;
            return this;
        }

        /**
         * @param dedicated The dedicated memory in megabytes (defaults
         * to `512`).
         * 
         * @return builder
         * 
         */
        public Builder dedicated(Integer dedicated) {
            return dedicated(Output.of(dedicated));
        }

        /**
         * @param swap The swap size in megabytes (defaults to `0`).
         * 
         * @return builder
         * 
         */
        public Builder swap(@Nullable Output<Integer> swap) {
            $.swap = swap;
            return this;
        }

        /**
         * @param swap The swap size in megabytes (defaults to `0`).
         * 
         * @return builder
         * 
         */
        public Builder swap(Integer swap) {
            return swap(Output.of(swap));
        }

        public ContainerMemoryArgs build() {
            return $;
        }
    }

}