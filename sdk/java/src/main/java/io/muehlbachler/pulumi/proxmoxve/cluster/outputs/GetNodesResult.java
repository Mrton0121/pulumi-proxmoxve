// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.Cluster.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Double;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetNodesResult {
    /**
     * @return The CPU count for each node.
     * 
     */
    private List<Integer> cpuCounts;
    /**
     * @return The CPU utilization on each node.
     * 
     */
    private List<Double> cpuUtilizations;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return The memory available on each node.
     * 
     */
    private List<Integer> memoryAvailables;
    /**
     * @return The memory used on each node.
     * 
     */
    private List<Integer> memoryUseds;
    /**
     * @return The node names.
     * 
     */
    private List<String> names;
    /**
     * @return Whether a node is online.
     * 
     */
    private List<Boolean> onlines;
    /**
     * @return The SSL fingerprint for each node.
     * 
     */
    private List<String> sslFingerprints;
    /**
     * @return The support level for each node.
     * 
     */
    private List<String> supportLevels;
    /**
     * @return The uptime in seconds for each node.
     * 
     */
    private List<Integer> uptimes;

    private GetNodesResult() {}
    /**
     * @return The CPU count for each node.
     * 
     */
    public List<Integer> cpuCounts() {
        return this.cpuCounts;
    }
    /**
     * @return The CPU utilization on each node.
     * 
     */
    public List<Double> cpuUtilizations() {
        return this.cpuUtilizations;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return The memory available on each node.
     * 
     */
    public List<Integer> memoryAvailables() {
        return this.memoryAvailables;
    }
    /**
     * @return The memory used on each node.
     * 
     */
    public List<Integer> memoryUseds() {
        return this.memoryUseds;
    }
    /**
     * @return The node names.
     * 
     */
    public List<String> names() {
        return this.names;
    }
    /**
     * @return Whether a node is online.
     * 
     */
    public List<Boolean> onlines() {
        return this.onlines;
    }
    /**
     * @return The SSL fingerprint for each node.
     * 
     */
    public List<String> sslFingerprints() {
        return this.sslFingerprints;
    }
    /**
     * @return The support level for each node.
     * 
     */
    public List<String> supportLevels() {
        return this.supportLevels;
    }
    /**
     * @return The uptime in seconds for each node.
     * 
     */
    public List<Integer> uptimes() {
        return this.uptimes;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetNodesResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<Integer> cpuCounts;
        private List<Double> cpuUtilizations;
        private String id;
        private List<Integer> memoryAvailables;
        private List<Integer> memoryUseds;
        private List<String> names;
        private List<Boolean> onlines;
        private List<String> sslFingerprints;
        private List<String> supportLevels;
        private List<Integer> uptimes;
        public Builder() {}
        public Builder(GetNodesResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cpuCounts = defaults.cpuCounts;
    	      this.cpuUtilizations = defaults.cpuUtilizations;
    	      this.id = defaults.id;
    	      this.memoryAvailables = defaults.memoryAvailables;
    	      this.memoryUseds = defaults.memoryUseds;
    	      this.names = defaults.names;
    	      this.onlines = defaults.onlines;
    	      this.sslFingerprints = defaults.sslFingerprints;
    	      this.supportLevels = defaults.supportLevels;
    	      this.uptimes = defaults.uptimes;
        }

        @CustomType.Setter
        public Builder cpuCounts(List<Integer> cpuCounts) {
            if (cpuCounts == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "cpuCounts");
            }
            this.cpuCounts = cpuCounts;
            return this;
        }
        public Builder cpuCounts(Integer... cpuCounts) {
            return cpuCounts(List.of(cpuCounts));
        }
        @CustomType.Setter
        public Builder cpuUtilizations(List<Double> cpuUtilizations) {
            if (cpuUtilizations == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "cpuUtilizations");
            }
            this.cpuUtilizations = cpuUtilizations;
            return this;
        }
        public Builder cpuUtilizations(Double... cpuUtilizations) {
            return cpuUtilizations(List.of(cpuUtilizations));
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder memoryAvailables(List<Integer> memoryAvailables) {
            if (memoryAvailables == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "memoryAvailables");
            }
            this.memoryAvailables = memoryAvailables;
            return this;
        }
        public Builder memoryAvailables(Integer... memoryAvailables) {
            return memoryAvailables(List.of(memoryAvailables));
        }
        @CustomType.Setter
        public Builder memoryUseds(List<Integer> memoryUseds) {
            if (memoryUseds == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "memoryUseds");
            }
            this.memoryUseds = memoryUseds;
            return this;
        }
        public Builder memoryUseds(Integer... memoryUseds) {
            return memoryUseds(List.of(memoryUseds));
        }
        @CustomType.Setter
        public Builder names(List<String> names) {
            if (names == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "names");
            }
            this.names = names;
            return this;
        }
        public Builder names(String... names) {
            return names(List.of(names));
        }
        @CustomType.Setter
        public Builder onlines(List<Boolean> onlines) {
            if (onlines == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "onlines");
            }
            this.onlines = onlines;
            return this;
        }
        public Builder onlines(Boolean... onlines) {
            return onlines(List.of(onlines));
        }
        @CustomType.Setter
        public Builder sslFingerprints(List<String> sslFingerprints) {
            if (sslFingerprints == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "sslFingerprints");
            }
            this.sslFingerprints = sslFingerprints;
            return this;
        }
        public Builder sslFingerprints(String... sslFingerprints) {
            return sslFingerprints(List.of(sslFingerprints));
        }
        @CustomType.Setter
        public Builder supportLevels(List<String> supportLevels) {
            if (supportLevels == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "supportLevels");
            }
            this.supportLevels = supportLevels;
            return this;
        }
        public Builder supportLevels(String... supportLevels) {
            return supportLevels(List.of(supportLevels));
        }
        @CustomType.Setter
        public Builder uptimes(List<Integer> uptimes) {
            if (uptimes == null) {
              throw new MissingRequiredPropertyException("GetNodesResult", "uptimes");
            }
            this.uptimes = uptimes;
            return this;
        }
        public Builder uptimes(Integer... uptimes) {
            return uptimes(List.of(uptimes));
        }
        public GetNodesResult build() {
            final var _resultValue = new GetNodesResult();
            _resultValue.cpuCounts = cpuCounts;
            _resultValue.cpuUtilizations = cpuUtilizations;
            _resultValue.id = id;
            _resultValue.memoryAvailables = memoryAvailables;
            _resultValue.memoryUseds = memoryUseds;
            _resultValue.names = names;
            _resultValue.onlines = onlines;
            _resultValue.sslFingerprints = sslFingerprints;
            _resultValue.supportLevels = supportLevels;
            _resultValue.uptimes = uptimes;
            return _resultValue;
        }
    }
}