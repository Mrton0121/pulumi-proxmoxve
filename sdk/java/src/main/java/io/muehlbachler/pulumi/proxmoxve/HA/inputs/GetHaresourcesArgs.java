// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.HA.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetHAResourcesArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetHAResourcesArgs Empty = new GetHAResourcesArgs();

    /**
     * The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
     * 
     */
    @Import(name="type")
    private @Nullable Output<String> type;

    /**
     * @return The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
     * 
     */
    public Optional<Output<String>> type() {
        return Optional.ofNullable(this.type);
    }

    private GetHAResourcesArgs() {}

    private GetHAResourcesArgs(GetHAResourcesArgs $) {
        this.type = $.type;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetHAResourcesArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetHAResourcesArgs $;

        public Builder() {
            $ = new GetHAResourcesArgs();
        }

        public Builder(GetHAResourcesArgs defaults) {
            $ = new GetHAResourcesArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param type The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
         * 
         * @return builder
         * 
         */
        public Builder type(@Nullable Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        public GetHAResourcesArgs build() {
            return $;
        }
    }

}