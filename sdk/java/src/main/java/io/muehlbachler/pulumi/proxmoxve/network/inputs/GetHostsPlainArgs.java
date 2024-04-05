// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.Network.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetHostsPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetHostsPlainArgs Empty = new GetHostsPlainArgs();

    /**
     * A node name.
     * 
     */
    @Import(name="nodeName", required=true)
    private String nodeName;

    /**
     * @return A node name.
     * 
     */
    public String nodeName() {
        return this.nodeName;
    }

    private GetHostsPlainArgs() {}

    private GetHostsPlainArgs(GetHostsPlainArgs $) {
        this.nodeName = $.nodeName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetHostsPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetHostsPlainArgs $;

        public Builder() {
            $ = new GetHostsPlainArgs();
        }

        public Builder(GetHostsPlainArgs defaults) {
            $ = new GetHostsPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param nodeName A node name.
         * 
         * @return builder
         * 
         */
        public Builder nodeName(String nodeName) {
            $.nodeName = nodeName;
            return this;
        }

        public GetHostsPlainArgs build() {
            if ($.nodeName == null) {
                throw new MissingRequiredPropertyException("GetHostsPlainArgs", "nodeName");
            }
            return $;
        }
    }

}