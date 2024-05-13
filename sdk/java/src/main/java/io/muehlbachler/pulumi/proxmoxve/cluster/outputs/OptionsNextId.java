// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.Cluster.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Integer;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class OptionsNextId {
    /**
     * @return The minimum number for the next free VM ID. Must be higher or equal to 100
     * 
     */
    private @Nullable Integer lower;
    /**
     * @return The maximum number for the next free VM ID. Must be less or equal to 999999999
     * 
     */
    private @Nullable Integer upper;

    private OptionsNextId() {}
    /**
     * @return The minimum number for the next free VM ID. Must be higher or equal to 100
     * 
     */
    public Optional<Integer> lower() {
        return Optional.ofNullable(this.lower);
    }
    /**
     * @return The maximum number for the next free VM ID. Must be less or equal to 999999999
     * 
     */
    public Optional<Integer> upper() {
        return Optional.ofNullable(this.upper);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(OptionsNextId defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Integer lower;
        private @Nullable Integer upper;
        public Builder() {}
        public Builder(OptionsNextId defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.lower = defaults.lower;
    	      this.upper = defaults.upper;
        }

        @CustomType.Setter
        public Builder lower(@Nullable Integer lower) {

            this.lower = lower;
            return this;
        }
        @CustomType.Setter
        public Builder upper(@Nullable Integer upper) {

            this.upper = upper;
            return this;
        }
        public OptionsNextId build() {
            final var _resultValue = new OptionsNextId();
            _resultValue.lower = lower;
            _resultValue.upper = upper;
            return _resultValue;
        }
    }
}