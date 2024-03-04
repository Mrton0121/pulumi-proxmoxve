// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.HA.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Map;
import java.util.Objects;

@CustomType
public final class GetHAGroupResult {
    /**
     * @return The comment associated with this group
     * 
     */
    private String comment;
    /**
     * @return The identifier of the High Availability group to read.
     * 
     */
    private String group;
    /**
     * @return The unique identifier of this resource.
     * 
     */
    private String id;
    /**
     * @return A flag that indicates that failing back to a higher priority node is disabled for this HA group.
     * 
     */
    private Boolean noFailback;
    /**
     * @return The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
     * 
     */
    private Map<String,Integer> nodes;
    /**
     * @return A flag that indicates that other nodes may not be used to run resources associated to this HA group.
     * 
     */
    private Boolean restricted;

    private GetHAGroupResult() {}
    /**
     * @return The comment associated with this group
     * 
     */
    public String comment() {
        return this.comment;
    }
    /**
     * @return The identifier of the High Availability group to read.
     * 
     */
    public String group() {
        return this.group;
    }
    /**
     * @return The unique identifier of this resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return A flag that indicates that failing back to a higher priority node is disabled for this HA group.
     * 
     */
    public Boolean noFailback() {
        return this.noFailback;
    }
    /**
     * @return The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
     * 
     */
    public Map<String,Integer> nodes() {
        return this.nodes;
    }
    /**
     * @return A flag that indicates that other nodes may not be used to run resources associated to this HA group.
     * 
     */
    public Boolean restricted() {
        return this.restricted;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetHAGroupResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String comment;
        private String group;
        private String id;
        private Boolean noFailback;
        private Map<String,Integer> nodes;
        private Boolean restricted;
        public Builder() {}
        public Builder(GetHAGroupResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.comment = defaults.comment;
    	      this.group = defaults.group;
    	      this.id = defaults.id;
    	      this.noFailback = defaults.noFailback;
    	      this.nodes = defaults.nodes;
    	      this.restricted = defaults.restricted;
        }

        @CustomType.Setter
        public Builder comment(String comment) {
            if (comment == null) {
              throw new MissingRequiredPropertyException("GetHAGroupResult", "comment");
            }
            this.comment = comment;
            return this;
        }
        @CustomType.Setter
        public Builder group(String group) {
            if (group == null) {
              throw new MissingRequiredPropertyException("GetHAGroupResult", "group");
            }
            this.group = group;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetHAGroupResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder noFailback(Boolean noFailback) {
            if (noFailback == null) {
              throw new MissingRequiredPropertyException("GetHAGroupResult", "noFailback");
            }
            this.noFailback = noFailback;
            return this;
        }
        @CustomType.Setter
        public Builder nodes(Map<String,Integer> nodes) {
            if (nodes == null) {
              throw new MissingRequiredPropertyException("GetHAGroupResult", "nodes");
            }
            this.nodes = nodes;
            return this;
        }
        @CustomType.Setter
        public Builder restricted(Boolean restricted) {
            if (restricted == null) {
              throw new MissingRequiredPropertyException("GetHAGroupResult", "restricted");
            }
            this.restricted = restricted;
            return this;
        }
        public GetHAGroupResult build() {
            final var _resultValue = new GetHAGroupResult();
            _resultValue.comment = comment;
            _resultValue.group = group;
            _resultValue.id = id;
            _resultValue.noFailback = noFailback;
            _resultValue.nodes = nodes;
            _resultValue.restricted = restricted;
            return _resultValue;
        }
    }
}