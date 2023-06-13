// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;


public final class GetDNSPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetDNSPlainArgs Empty = new GetDNSPlainArgs();

    @Import(name="nodeName", required=true)
    private String nodeName;

    public String nodeName() {
        return this.nodeName;
    }

    private GetDNSPlainArgs() {}

    private GetDNSPlainArgs(GetDNSPlainArgs $) {
        this.nodeName = $.nodeName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetDNSPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetDNSPlainArgs $;

        public Builder() {
            $ = new GetDNSPlainArgs();
        }

        public Builder(GetDNSPlainArgs defaults) {
            $ = new GetDNSPlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder nodeName(String nodeName) {
            $.nodeName = nodeName;
            return this;
        }

        public GetDNSPlainArgs build() {
            $.nodeName = Objects.requireNonNull($.nodeName, "expected parameter 'nodeName' to be non-null");
            return $;
        }
    }

}