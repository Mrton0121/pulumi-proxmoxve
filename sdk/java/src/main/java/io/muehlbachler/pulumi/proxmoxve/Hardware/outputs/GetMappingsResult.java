// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.Hardware.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import io.muehlbachler.pulumi.proxmoxve.Hardware.outputs.GetMappingsCheck;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetMappingsResult {
    /**
     * @return The name of the node whose configurations should be checked for correctness.
     * 
     */
    private @Nullable String checkNode;
    /**
     * @return Might contain relevant diagnostics about incorrect configurations.
     * 
     */
    private List<GetMappingsCheck> checks;
    /**
     * @return The unique identifier of this hardware mappings data source.
     * 
     */
    private String id;
    /**
     * @return The identifiers of the hardware mappings.
     * 
     */
    private List<String> ids;
    /**
     * @return The type of the hardware mappings.
     * 
     */
    private String type;

    private GetMappingsResult() {}
    /**
     * @return The name of the node whose configurations should be checked for correctness.
     * 
     */
    public Optional<String> checkNode() {
        return Optional.ofNullable(this.checkNode);
    }
    /**
     * @return Might contain relevant diagnostics about incorrect configurations.
     * 
     */
    public List<GetMappingsCheck> checks() {
        return this.checks;
    }
    /**
     * @return The unique identifier of this hardware mappings data source.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return The identifiers of the hardware mappings.
     * 
     */
    public List<String> ids() {
        return this.ids;
    }
    /**
     * @return The type of the hardware mappings.
     * 
     */
    public String type() {
        return this.type;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetMappingsResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String checkNode;
        private List<GetMappingsCheck> checks;
        private String id;
        private List<String> ids;
        private String type;
        public Builder() {}
        public Builder(GetMappingsResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.checkNode = defaults.checkNode;
    	      this.checks = defaults.checks;
    	      this.id = defaults.id;
    	      this.ids = defaults.ids;
    	      this.type = defaults.type;
        }

        @CustomType.Setter
        public Builder checkNode(@Nullable String checkNode) {

            this.checkNode = checkNode;
            return this;
        }
        @CustomType.Setter
        public Builder checks(List<GetMappingsCheck> checks) {
            if (checks == null) {
              throw new MissingRequiredPropertyException("GetMappingsResult", "checks");
            }
            this.checks = checks;
            return this;
        }
        public Builder checks(GetMappingsCheck... checks) {
            return checks(List.of(checks));
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetMappingsResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder ids(List<String> ids) {
            if (ids == null) {
              throw new MissingRequiredPropertyException("GetMappingsResult", "ids");
            }
            this.ids = ids;
            return this;
        }
        public Builder ids(String... ids) {
            return ids(List.of(ids));
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("GetMappingsResult", "type");
            }
            this.type = type;
            return this;
        }
        public GetMappingsResult build() {
            final var _resultValue = new GetMappingsResult();
            _resultValue.checkNode = checkNode;
            _resultValue.checks = checks;
            _resultValue.id = id;
            _resultValue.ids = ids;
            _resultValue.type = type;
            return _resultValue;
        }
    }
}
