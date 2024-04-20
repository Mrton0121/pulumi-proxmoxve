// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.Hardware.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetMappingsCheck {
    /**
     * @return The corresponding hardware mapping ID of the node check diagnostic entry.
     * 
     */
    private String mappingId;
    /**
     * @return The message of the node check diagnostic entry.
     * 
     */
    private String message;
    /**
     * @return The severity of the node check diagnostic entry.
     * 
     */
    private String severity;

    private GetMappingsCheck() {}
    /**
     * @return The corresponding hardware mapping ID of the node check diagnostic entry.
     * 
     */
    public String mappingId() {
        return this.mappingId;
    }
    /**
     * @return The message of the node check diagnostic entry.
     * 
     */
    public String message() {
        return this.message;
    }
    /**
     * @return The severity of the node check diagnostic entry.
     * 
     */
    public String severity() {
        return this.severity;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetMappingsCheck defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String mappingId;
        private String message;
        private String severity;
        public Builder() {}
        public Builder(GetMappingsCheck defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.mappingId = defaults.mappingId;
    	      this.message = defaults.message;
    	      this.severity = defaults.severity;
        }

        @CustomType.Setter
        public Builder mappingId(String mappingId) {
            if (mappingId == null) {
              throw new MissingRequiredPropertyException("GetMappingsCheck", "mappingId");
            }
            this.mappingId = mappingId;
            return this;
        }
        @CustomType.Setter
        public Builder message(String message) {
            if (message == null) {
              throw new MissingRequiredPropertyException("GetMappingsCheck", "message");
            }
            this.message = message;
            return this;
        }
        @CustomType.Setter
        public Builder severity(String severity) {
            if (severity == null) {
              throw new MissingRequiredPropertyException("GetMappingsCheck", "severity");
            }
            this.severity = severity;
            return this;
        }
        public GetMappingsCheck build() {
            final var _resultValue = new GetMappingsCheck();
            _resultValue.mappingId = mappingId;
            _resultValue.message = message;
            _resultValue.severity = severity;
            return _resultValue;
        }
    }
}
