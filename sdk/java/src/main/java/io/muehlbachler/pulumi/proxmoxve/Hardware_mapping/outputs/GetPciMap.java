// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.Hardware_mapping.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetPciMap {
    /**
     * @return The comment of the mapped PCI device.
     * 
     */
    private String comment;
    /**
     * @return The ID attribute of the map.
     * 
     */
    private String id;
    /**
     * @return The IOMMU group attribute of the map.
     * 
     */
    private Integer iommuGroup;
    /**
     * @return The node name attribute of the map.
     * 
     */
    private String node;
    /**
     * @return The path attribute of the map.
     * 
     */
    private String path;
    /**
     * @return The subsystem ID attribute of the map.Not mandatory for the Proxmox VE API call, but causes a PCI hardware mapping to be incomplete when not set.
     * 
     */
    private String subsystemId;

    private GetPciMap() {}
    /**
     * @return The comment of the mapped PCI device.
     * 
     */
    public String comment() {
        return this.comment;
    }
    /**
     * @return The ID attribute of the map.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return The IOMMU group attribute of the map.
     * 
     */
    public Integer iommuGroup() {
        return this.iommuGroup;
    }
    /**
     * @return The node name attribute of the map.
     * 
     */
    public String node() {
        return this.node;
    }
    /**
     * @return The path attribute of the map.
     * 
     */
    public String path() {
        return this.path;
    }
    /**
     * @return The subsystem ID attribute of the map.Not mandatory for the Proxmox VE API call, but causes a PCI hardware mapping to be incomplete when not set.
     * 
     */
    public String subsystemId() {
        return this.subsystemId;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetPciMap defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String comment;
        private String id;
        private Integer iommuGroup;
        private String node;
        private String path;
        private String subsystemId;
        public Builder() {}
        public Builder(GetPciMap defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.comment = defaults.comment;
    	      this.id = defaults.id;
    	      this.iommuGroup = defaults.iommuGroup;
    	      this.node = defaults.node;
    	      this.path = defaults.path;
    	      this.subsystemId = defaults.subsystemId;
        }

        @CustomType.Setter
        public Builder comment(String comment) {
            if (comment == null) {
              throw new MissingRequiredPropertyException("GetPciMap", "comment");
            }
            this.comment = comment;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetPciMap", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder iommuGroup(Integer iommuGroup) {
            if (iommuGroup == null) {
              throw new MissingRequiredPropertyException("GetPciMap", "iommuGroup");
            }
            this.iommuGroup = iommuGroup;
            return this;
        }
        @CustomType.Setter
        public Builder node(String node) {
            if (node == null) {
              throw new MissingRequiredPropertyException("GetPciMap", "node");
            }
            this.node = node;
            return this;
        }
        @CustomType.Setter
        public Builder path(String path) {
            if (path == null) {
              throw new MissingRequiredPropertyException("GetPciMap", "path");
            }
            this.path = path;
            return this;
        }
        @CustomType.Setter
        public Builder subsystemId(String subsystemId) {
            if (subsystemId == null) {
              throw new MissingRequiredPropertyException("GetPciMap", "subsystemId");
            }
            this.subsystemId = subsystemId;
            return this;
        }
        public GetPciMap build() {
            final var _resultValue = new GetPciMap();
            _resultValue.comment = comment;
            _resultValue.id = id;
            _resultValue.iommuGroup = iommuGroup;
            _resultValue.node = node;
            _resultValue.path = path;
            _resultValue.subsystemId = subsystemId;
            return _resultValue;
        }
    }
}