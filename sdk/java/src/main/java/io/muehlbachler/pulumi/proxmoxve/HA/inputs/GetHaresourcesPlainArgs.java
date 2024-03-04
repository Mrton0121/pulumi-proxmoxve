// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.HA.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetHAResourcesPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetHAResourcesPlainArgs Empty = new GetHAResourcesPlainArgs();

    /**
     * The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
     * 
     */
    @Import(name="type")
    private @Nullable String type;

    /**
     * @return The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
     * 
     */
    public Optional<String> type() {
        return Optional.ofNullable(this.type);
    }

    private GetHAResourcesPlainArgs() {}

    private GetHAResourcesPlainArgs(GetHAResourcesPlainArgs $) {
        this.type = $.type;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetHAResourcesPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetHAResourcesPlainArgs $;

        public Builder() {
            $ = new GetHAResourcesPlainArgs();
        }

        public Builder(GetHAResourcesPlainArgs defaults) {
            $ = new GetHAResourcesPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param type The type of High Availability resources to fetch (`vm` or `ct`). All resources will be fetched if this option is unset.
         * 
         * @return builder
         * 
         */
        public Builder type(@Nullable String type) {
            $.type = type;
            return this;
        }

        public GetHAResourcesPlainArgs build() {
            return $;
        }
    }

}